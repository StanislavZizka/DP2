"""
Helper functions and utilities for the texture generator application.
"""
import re
from typing import Dict, Any, Tuple
from config import TEXTURE_DEFAULTS

def hex_to_rgb(hex_color: str) -> Tuple[float, float, float]:
    """
    Convert HEX color to RGB tuple with values in [0, 1] range.
    
    Args:
        hex_color: Color in HEX format (e.g., "#ff0000" or "ff0000")
        
    Returns:
        tuple: RGB values as floats in range [0, 1]
    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError(f"Invalid HEX color format: {hex_color}")
    
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def validate_hex_color(color: str) -> bool:
    """
    Validate if string is a valid HEX color.
    
    Args:
        color: Color string to validate
        
    Returns:
        bool: True if valid HEX color, False otherwise
    """
    if not isinstance(color, str):
        return False
    
    # Remove # if present
    color = color.lstrip("#")
    
    # Check if it's exactly 6 characters and all are valid hex
    return len(color) == 6 and re.match(r'^[0-9a-fA-F]+$', color) is not None

def validate_texture_params(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate texture generation parameters.
    
    Args:
        data: Dictionary containing texture parameters
        
    Returns:
        dict: Dictionary with 'valid' boolean, 'params' dict, and optional 'error' string
    """
    try:
        # Extract parameters with defaults
        K = float(data.get('K', TEXTURE_DEFAULTS['K']))
        t_max = float(data.get('t_max', TEXTURE_DEFAULTS['t_max']))
        delta_t = float(data.get('delta_t', TEXTURE_DEFAULTS['delta_t']))
        color1 = data.get('color1', TEXTURE_DEFAULTS['color1'])
        color2 = data.get('color2', TEXTURE_DEFAULTS['color2'])
        
        # Validate ranges
        if not (0.1 <= K <= 5.0):
            return {'valid': False, 'error': 'K must be between 0.1 and 5.0'}
        
        if not (1.0 <= t_max <= 10000.0):
            return {'valid': False, 'error': 't_max must be between 1.0 and 10000.0'}
        
        if not (0.001 <= delta_t <= 1.0):
            return {'valid': False, 'error': 'delta_t must be between 0.001 and 1.0'}
        
        if delta_t > t_max:
            return {'valid': False, 'error': 'delta_t cannot be greater than t_max'}
        
        # Validate colors
        if not validate_hex_color(color1):
            return {'valid': False, 'error': f'Invalid color1 format: {color1}'}
        
        if not validate_hex_color(color2):
            return {'valid': False, 'error': f'Invalid color2 format: {color2}'}
        
        return {
            'valid': True,
            'params': {
                'K': K,
                't_max': t_max,
                'delta_t': delta_t,
                'color1': color1,
                'color2': color2
            }
        }
        
    except (ValueError, TypeError) as e:
        return {'valid': False, 'error': f'Invalid parameter type: {str(e)}'}

def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        str: Formatted size string (e.g., "1.5 MB")
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"

def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp value between min and max.
    
    Args:
        value: Value to clamp
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        
    Returns:
        float: Clamped value
    """
    return max(min_val, min(value, max_val))