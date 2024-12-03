# utils.py

from django.conf import settings

def setup_cloudinary(cloud_name, api_key, api_secret):
    # Set up Cloudinary configurations
    settings.CLOUDINARY_STORAGE = {
        'CLOUD_NAME': cloud_name,
        'API_KEY': api_key,
        'API_SECRET': api_secret,
    }
    settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.MediaStorage'
    settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.StaticStorage'
    
    # Import cloudinary after settings have been defined to avoid circular import
    import cloudinary
    cloudinary.config(
        cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
        api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
        api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
    )
