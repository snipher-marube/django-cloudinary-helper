from django.conf import settings
from django.core.files.storage import Storage
import cloudinary.uploader
from django.core.files.storage import FileSystemStorage
from cloudinary import CloudinaryImage
import os


class CloudinaryMediaStorage(Storage):
    """Custom storage for Cloudinary Media Files."""
    def _save(self, name, content):
        # Ensure the name is valid for Cloudinary
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name)
        return response["public_id"]

    def url(self, name):
        return CloudinaryImage(name).build_url()

    def exists(self, name):
        """Check if a file exists in Cloudinary."""
        try:
            CloudinaryImage(name).build_url()  # This will raise an error if the file doesn't exist.
            return True
        except Exception:
            return False


class CloudinaryStaticStorage(Storage):
    """Custom storage for Cloudinary Static Files."""
    def _save(self, name, content):
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name, resource_type="raw")
        return response["public_id"]

    def url(self, name):
        return CloudinaryImage(name).build_url()

    def exists(self, name):
        """Check if a file exists in Cloudinary."""
        try:
            CloudinaryImage(name).build_url()
            return True
        except Exception:
            return False


def is_production():
    """Helper function to determine if the environment is production."""
    return not settings.DEBUG


def get_storage_class():
    """Return the appropriate storage class."""
    if is_production():
        return CloudinaryMediaStorage
    return FileSystemStorage
