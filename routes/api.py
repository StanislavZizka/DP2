"""
API routes for handling AJAX requests and data processing.
Handles all routes that return JSON responses.
"""
from flask import Blueprint, request, jsonify, url_for
from services.texture_generator import TextureGeneratorService
from utils.helpers import validate_texture_params

# Create Blueprint for API routes
api = Blueprint('api', __name__)

# Initialize texture generation service
texture_service = TextureGeneratorService()

@api.route('/calculate', methods=['POST'])
def calculate():
    """
    Generate texture based on provided parameters.
    
    Expected JSON payload:
    {
        "K": float,
        "t_max": float,
        "delta_t": float,
        "color1": string (hex),
        "color2": string (hex)
    }
    
    Returns:
    {
        "image_url": string
    } or {"error": string}
    """
    try:
        # Get and validate request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate parameters
        validation_result = validate_texture_params(data)
        if not validation_result['valid']:
            return jsonify({'error': validation_result['error']}), 400
        
        params = validation_result['params']
        
        # Generate texture using service
        image_path = texture_service.generate_activator_inhibitor(
            K=params['K'],
            t_max=params['t_max'],
            delta_t=params['delta_t'],
            color1=params['color1'],
            color2=params['color2']
        )
        
        # Return image URL
        image_url = url_for('static', filename='images/activator_inhibitor_texture.png', _external=True)
        return jsonify({'image_url': image_url})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500