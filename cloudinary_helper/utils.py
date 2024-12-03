import os
import cloudinary
from django.conf import settings

def setup_cloudinary():
    """Configure Cloudinary settings based on environment variables or settings."""
    
    # First, try to get Cloudinary config from environment variables
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
    api_key = os.getenv('CLOUDINARY_API_KEY')
    api_secret = os.getenv('CLOUDINARY_API_SECRET')

    # If not found in environment variables, fall back to Django settings
    if not cloud_name:
        cloud_name = getattr(settings, 'CLOUDINARY_CLOUD_NAME', None)
    if not api_key:
        api_key = getattr(settings, 'CLOUDINARY_API_KEY', None)
    if not api_secret:
        api_secret = getattr(settings, 'CLOUDINARY_API_SECRET', None)

    # Ensure all necessary environment variables or settings are provided
    if not cloud_name or not api_key or not api_secret:
        raise ValueError("Cloudinary configuration is incomplete. Please check your environment variables or settings.")

    # Configure Cloudinary with the values
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    # Set the Cloudinary storage for media and static files if not already set
    if not hasattr(settings, 'DEFAULT_FILE_STORAGE'):
        settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
    if not hasattr(settings, 'STATICFILES_STORAGE'):
        settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'
