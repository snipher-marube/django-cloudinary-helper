from django.conf import settings
from django.core.files.storage import FileSystemStorage
import cloudinary.uploader
from cloudinary import CloudinaryImage
import os


class CloudinaryMediaStorage(FileSystemStorage):
    """Custom storage for Cloudinary Media Files."""
    def _save(self, name, content):
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name)
        return response['public_id']

    def url(self, name):
        return CloudinaryImage(name).build_url()


class CloudinaryStaticStorage(FileSystemStorage):
    """Custom storage for Cloudinary Static Files."""
    def _save(self, name, content):
        name = os.path.basename(name)
        response = cloudinary.uploader.upload(content, public_id=name, resource_type="raw")
        return response['public_id']

    def url(self, name):
        return CloudinaryImage(name).build_url()
