import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config
from django.conf import settings

def setup_cloudinary(cloud_name, api_key, api_secret):
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    
    settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
    settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'
