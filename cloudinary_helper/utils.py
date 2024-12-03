import os
import cloudinary
from django.conf import settings

def setup_cloudinary():
    """Configure Cloudinary settings based on environment variables or settings."""
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME', settings.CLOUDINARY_CLOUD_NAME)
    api_key = os.getenv('CLOUDINARY_API_KEY', settings.CLOUDINARY_API_KEY)
    api_secret = os.getenv('CLOUDINARY_API_SECRET', settings.CLOUDINARY_API_SECRET)

    # Configure Cloudinary with either environment variables or Django settings
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    # Ensure Cloudinary storage is set in settings
    if not hasattr(settings, 'DEFAULT_FILE_STORAGE'):
        settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
    if not hasattr(settings, 'STATICFILES_STORAGE'):
        settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'
