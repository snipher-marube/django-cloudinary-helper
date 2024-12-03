import cloudinary.uploader
import cloudinary.api
from django.conf import settings

def setup_cloudinary(cloud_name, api_key, api_secret):
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    
    # Set the file storage settings to use Cloudinary
    if not settings.DEFAULT_FILE_STORAGE:
        settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
    if not settings.STATICFILES_STORAGE:
        settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'