import os
from os import environ

# Base configuration class with default settings
class Config(object):

    # Disable debug and testing mode by default
    DEBUG = False
    TESTING = False

    # Get the absolute path of the directory containing this file
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Secret key for session management and other security-related uses
    SECRET_KEY = 'kiarashkiani79'
    
    # Path for file uploads
    UPLOADS = "/Flask_App/app/static/uploads"

    # Ensure session cookies are only sent over HTTPS
    SESSION_COOKIE_SECURE = True
    
    # Default theme setting, can be overridden in subclasses
    DEFAULT_THEME = None

# Configuration class for development environment
class DevelopmentConfig(Config):
    # Enable debug mode for development
    DEBUG = True
    
    # Allow session cookies to be sent over HTTP (useful for local development)
    SESSION_COOKIE_SECURE = False

# Configuration class for debug environment
class DebugConfig(Config):
    # Disable debug mode for this configuration
    DEBUG = False
