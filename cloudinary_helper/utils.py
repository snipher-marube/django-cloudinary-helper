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

    if not settings.DEBUG:
        replace_fields_with_cloudinary()


def replace_fields_with_cloudinary():
    """
    Replace `ImageField` and `FileField` with `CloudinaryField` in all models if DEBUG is False.
    """
    from django.apps import apps
    all_models = apps.get_models()

    for model in all_models:
        for field_name, field in model._meta.fields_map.items():
            if isinstance(field, ImageField):
                # Replace ImageField with CloudinaryField for images
                setattr(model, field_name, CloudinaryField('image'))
            elif isinstance(field, FileField):
                # Replace FileField with CloudinaryField for files
                setattr(model, field_name, CloudinaryField('file'))
