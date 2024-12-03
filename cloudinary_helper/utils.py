from django.conf import settings
from cloudinary.models import CloudinaryField
from django.db.models import ImageField, FileField


def setup_cloudinary(cloud_name, api_key, api_secret):
    # Set up Cloudinary configurations
    settings.CLOUDINARY_STORAGE = {
        'CLOUD_NAME': cloud_name,
        'API_KEY': api_key,
        'API_SECRET': api_secret,
    }
    settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.MediaStorage'
    settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.StaticStorage'
    settings.CLOUDINARY_URL_CONFIG = {
        'secure': True
    }


    



