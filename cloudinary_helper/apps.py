from django.apps import AppConfig
from django.conf import settings

class CloudinaryHelperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cloudinary_helper'

    def ready(self):
        if not settings.DEBUG:
            from cloudinary_helper.utils import replace_fields_with_cloudinary
            replace_fields_with_cloudinary()
