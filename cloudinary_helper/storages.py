from django.conf import settings
from django.core.files.storage import Storage
import cloudinary.uploader
from cloudinary import CloudinaryImage
import os
from django.core.files.storage import FileSystemStorage

class CloudinaryMediaStorage(Storage):
    """Custom storage for Cloudinary Media Files."""
    def _save(self, name, content):
        # Ensure the name is valid for Cloudinary
        name = os.path.basename(name)

        # Asynchronous upload to Cloudinary with specified upload preset (optional)
        response = cloudinary.uploader.upload(content, 
                                              public_id=name, 
                                              resource_type="auto",  # auto-detect file type
                                              eager=[{'width': 800, 'height': 800, 'crop': 'limit'}],  # Example transformation
                                              upload_preset="media_preset" if settings.CLOUDINARY_MEDIA_PRESET else None)  # Optional preset

        return response["public_id"]

    def url(self, name):
        # Return the URL for the file in Cloudinary
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

        # Asynchronous upload for static files
        response = cloudinary.uploader.upload(content, 
                                              public_id=name, 
                                              resource_type="raw",  # Raw file type for static assets
                                              eager=[{'width': 1024, 'height': 1024, 'crop': 'limit'}],  # Example transformation
                                              upload_preset="static_preset" if settings.CLOUDINARY_STATIC_PRESET else None)

        return response["public_id"]

    def url(self, name):
        # Return the URL for static files
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
