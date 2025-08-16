"""
Mathematical Texture Generator Flask Application

A clean, organized Flask application for generating mathematical textures
using reaction-diffusion models with an intuitive web interface.
"""
import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for serverless deployment

from flask import Flask
from config import config
from routes.pages import pages
from routes.api import api

def create_app(config_name=None):
    """
    Flask application factory pattern.
    
    Args:
        config_name: Configuration environment ('development', 'production', 'testing')
        
    Returns:
        Flask: Configured Flask application instance
    """
    # Determine configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    # Create Flask app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(pages)
    app.register_blueprint(api)
    
    # Add error handlers
    register_error_handlers(app)
    
    return app

def register_error_handlers(app):
    """Register custom error handlers for the application."""
    
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 'Page not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    @app.errorhandler(400)
    def bad_request_error(error):
        return {'error': 'Bad request'}, 400

# Create app instance
app = create_app()

# For Vercel serverless deployment
application = app

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)