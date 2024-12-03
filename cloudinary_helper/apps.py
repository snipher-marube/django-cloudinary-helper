from django.apps import AppConfig
from django.conf import settings
from django.db.models.fields.files import FileField, ImageField
from cloudinary.models import CloudinaryField

class CloudinaryHelperConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cloudinary_helper"

    def ready(self):
        # Automatically replace fields in production
        if not settings.DEBUG:
            # Replace default fields with CloudinaryField
            FileField.__class__ = CloudinaryField
            ImageField.__class__ = CloudinaryField
