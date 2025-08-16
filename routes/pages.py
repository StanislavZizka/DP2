"""
Page routes for rendering HTML templates.
Handles all routes that return rendered HTML pages.
"""
from flask import Blueprint, render_template, send_from_directory

# Create Blueprint for page routes
pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@pages.route('/activator_inhibitor')
def activator_inhibitor():
    """Render the activator-inhibitor texture generation page."""
    return render_template('activator_inhibitor.html')

@pages.route('/assets/<path:filename>')
def assets(filename):
    """Serve static assets (3D models, etc.)."""
    return send_from_directory('assets', filename)