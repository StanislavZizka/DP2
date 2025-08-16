"""
Configuration settings for the Mathematical Texture Generator application.
"""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
ASSETS_DIR = BASE_DIR / "assets"

# Image settings
IMAGES_DIR = STATIC_DIR / "images"
DEFAULT_TEXTURE_SIZE = 512
SUPPORTED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg']

# Texture generation settings
TEXTURE_DEFAULTS = {
    'K': 1.0,
    't_max': 10.0,
    'delta_t': 0.1,
    'color1': '#0000ff',
    'color2': '#ff0000'
}

# Simulation parameters
SIMULATION_PARAMS = {
    'D_a': 0.02,  # Activator diffusion
    'D_b': 0.1,   # Inhibitor diffusion (5x higher than D_a)
    'feed_rate': 0.035,  # Activator production
    'kill_rate': 0.06,   # Inhibitor removal
    'random_seed': 42
}

# 3D Model settings
SHELL_MODELS = {
    'buccinidae': 'Buccinidae/Buccinidae.obj',
    'fasciolariidae': 'Fasciolariidae/Fasciolariidae.obj',
    'moon-snail': 'Moon snail/Moon snail.obj',
    'muricidae': 'Muricidae/Muricidae.obj',
    'pecten': 'Pecten/Pecten.obj',
    'whelk': 'Whelk/Whelk.obj'
}

# Flask configuration
class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}