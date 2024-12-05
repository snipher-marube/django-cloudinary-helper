from django.conf import settings
from django.core.files.storage import Storage, FileSystemStorage
import cloudinary.uploader
from cloudinary import CloudinaryImage
import os
from PIL import Image
from io import BytesIO

class CloudinaryMediaStorage(Storage):
    """Custom storage for Cloudinary Media Files."""
    def _compress_image(self, content):
        """Compress the image before uploading."""
        image = Image.open(content)
        output = BytesIO()
        image.save(output, format='JPEG', quality=85)  
        output.seek(0)
        return output

    def _save(self, name, content):
        name = os.path.basename(name)
        content = self._compress_image(content)

        response = cloudinary.uploader.upload(
            content,
            public_id=name,
            resource_type="auto",
            eager=[{'width': 400, 'height': 400, 'crop': 'fill'}],  # Lightweight transformation
            upload_preset="media_preset" if getattr(settings, 'CLOUDINARY_MEDIA_PRESET', None) else None
        )
        return response["public_id"]

    def url(self, name):
        return CloudinaryImage(name).build_url()

    def exists(self, name):
        try:
            CloudinaryImage(name).build_url()
            return True
        except Exception:
            return False

class CloudinaryStaticStorage(Storage):
    """Custom storage for Cloudinary Static Files."""
    def _save(self, name, content):
        name = os.path.basename(name)

        response = cloudinary.uploader.upload(
            content,
            public_id=name,
            resource_type="raw",
            eager=[{'width': 1024, 'height': 1024, 'crop': 'limit'}],
            upload_preset="static_preset" if getattr(settings, 'CLOUDINARY_STATIC_PRESET', None) else None
        )
        return response["public_id"]

    def url(self, name):
        return CloudinaryImage(name).build_url()

    def exists(self, name):
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
    return CloudinaryMediaStorage if is_production() else FileSystemStorage
