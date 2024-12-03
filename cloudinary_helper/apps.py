from django.apps import AppConfig
from django.conf import settings
from .utils import setup_cloudinary

class CloudinaryHelperConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cloudinary_helper"

    def ready(self):
        # Ensure CLOUDINARY_STORAGE is set before accessing it
        if not hasattr(settings, 'CLOUDINARY_STORAGE'):
            raise AttributeError("CLOUDINARY_STORAGE is not defined in the settings.")
        
        if not settings.DEBUG:
            # Automatically configure Cloudinary in production
            setup_cloudinary(
                settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
                settings.CLOUDINARY_STORAGE['API_KEY'],
                settings.CLOUDINARY_STORAGE['API_SECRET']
            )

