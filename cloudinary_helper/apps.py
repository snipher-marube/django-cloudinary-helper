from django.apps import AppConfig
from decouple import config
from django.conf import settings
from .utils import setup_cloudinary

class CloudinaryHelperConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cloudinary_helper"

    def ready(self):
        if not settings.DEBUG:
            setup_cloudinary(
                config('CLOUDINARY_CLOUD_NAME'),
                config('CLOUDINARY_API_KEY'),
                config('CLOUDINARY_API_SECRET')
            )
