import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

def setup_cloudinary(cloud_name, api_key, api_secret):
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )
    settings.DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
    settings.STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'

    DEFAULT_UPLOAD_OPTIONS = {
        "folder": "default",
        "overwrite": True,
        "resource_type": "auto"
    }

    return DEFAULT_UPLOAD_OPTIONS

def upload_image(image, options=None):
    if options is None:
        options = {}

    upload_options = {**options}

    return cloudinary.uploader.upload(image, **upload_options)

def delete_image(public_id):
    return cloudinary.uploader.destroy(public_id)

def get_image(public_id):
    return cloudinary.api.resource(public_id)

def get_images():
    return cloudinary.api.resources()

def get_image_url(public_id):
    return cloudinary.utils.cloudinary_url(public_id)[0]

def get_image_thumbnail_url(public_id, width, height):
    return cloudinary.utils.cloudinary_url(public_id, width=width, height=height, crop="fill")[0]

def get_image_responsive_url(public_id, width, height):
    return cloudinary.utils.cloudinary_url(public_id, width=width, height=height, crop="fill", responsive=True)[0]

def get_image_responsive_srcset(public_id, width, height):
    return cloudinary.utils.cloudinary_url(public_id, width=width, height=height, crop="fill", responsive=True)[1]

def get_image_responsive_sizes():
    return "(min-width: 768px) 50vw, 100vw"

def get_image_responsive_image(public_id, width, height):
    return f'<img src="{get_image_responsive_url(public_id, width, height)}" srcset="{get_image_responsive_srcset(public_id, width, height)}" sizes="{get_image_responsive_sizes()}" alt="{public_id}">'
