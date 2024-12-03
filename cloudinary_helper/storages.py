from django.conf import settings
from django.core.files.storage import FileSystemStorage
import cloudinary
import cloudinary.uploader
from django.core.files.storage import Storage
from cloudinary import CloudinaryImage
import os



class CloudinaryMediaStorage(Storage):
    """Custom storage for Cloudinary Media Files."""
    def _save(self, name, content):
        # Ensure the name is valid for Cloudinary public ID
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name)
        return response['public_id']

    def url(self, name):
        # Generate the URL for the stored file
        return CloudinaryImage(name).build_url()


class CloudinaryStaticStorage(Storage):
    """Custom storage for Cloudinary Static Files."""
    def _save(self, name, content):
        # Ensure the name is valid for Cloudinary public ID
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name, resource_type="raw")
        return response['public_id']

    def url(self, name):
        # Generate the URL for the static file
        return CloudinaryImage(name).build_url()


class StaticStorage(FileSystemStorage):
    """Custom Static Storage class that switches based on DEBUG setting."""
    def __init__(self, *args, **kwargs):
        if settings.DEBUG:
            location = settings.STATICFILES_DIRS[0]  # Location from settings when in DEBUG mode
        else:
            location = None  # Cloudinary will handle location when not in DEBUG mode
        super().__init__(location=location, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if settings.DEBUG:
            # For DEBUG, create the normal static storage
            return super().__new__(cls, *args, **kwargs)
        else:
            # For non-DEBUG, create Cloudinary static storage
            return CloudinaryStaticStorage(*args, **kwargs)


class MediaStorage(FileSystemStorage):
    """Custom Media Storage class that switches based on DEBUG setting."""
    def __init__(self, *args, **kwargs):
        if settings.DEBUG:
            location = settings.MEDIA_ROOT  # Location from settings when in DEBUG mode
        else:
            location = None  # Cloudinary will handle location when not in DEBUG mode
        super().__init__(location=location, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if settings.DEBUG:
            # For DEBUG, create the normal media storage
            return super().__new__(cls, *args, **kwargs)
        else:
            # For non-DEBUG, create Cloudinary media storage
            return CloudinaryMediaStorage(*args, **kwargs)
