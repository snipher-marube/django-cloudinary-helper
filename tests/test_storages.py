import unittest
from unittest.mock import patch
from django.conf import settings
from cloudinary_helper.storages import StaticStorage, MediaStorage


class TestStorages(unittest.TestCase):

    def setUp(self):
        # Backup original settings
        self.original_debug = settings.DEBUG
        self.original_staticfiles_dirs = getattr(settings, "STATICFILES_DIRS", [])
        self.original_media_root = getattr(settings, "MEDIA_ROOT", "/tmp")

        # Mock settings
        settings.STATICFILES_DIRS = ["/mock/static/"]
        settings.MEDIA_ROOT = "/mock/media/"

    def tearDown(self):
        # Restore original settings
        settings.DEBUG = self.original_debug
        settings.STATICFILES_DIRS = self.original_staticfiles_dirs
        settings.MEDIA_ROOT = self.original_media_root

    def test_debug_static_storage(self):
        settings.DEBUG = True
        storage = StaticStorage()
        self.assertEqual(storage.__class__.__name__, "FileSystemStorage")
        self.assertEqual(storage.location, "/mock/static/")  # Add the trailing slash

    def test_production_static_storage(self):
        settings.DEBUG = False
        storage = StaticStorage()
        self.assertEqual(storage.__class__.__name__, "CloudinaryStaticStorage")

    def test_debug_media_storage(self):
        settings.DEBUG = True
        storage = MediaStorage()
        self.assertEqual(storage.__class__.__name__, "FileSystemStorage")
        self.assertEqual(storage.location, "/mock/media/")  # Add the trailing slash
    
    def test_production_media_storage(self):
        settings.DEBUG = False
        storage = MediaStorage()
        self.assertEqual(storage.__class__.__name__, "CloudinaryMediaStorage")


class TestSetupCloudinary(unittest.TestCase):

    @patch("cloudinary_helper.utils.settings")
    def test_setup_cloudinary(self, mock_settings):
        from cloudinary_helper.utils import setup_cloudinary

        # Mock credentials
        cloud_name = "mock_cloud_name"
        api_key = "mock_api_key"
        api_secret = "mock_api_secret"

        setup_cloudinary(cloud_name, api_key, api_secret)

        # Verify settings were updated correctly
        self.assertEqual(
            mock_settings.CLOUDINARY_STORAGE,
            {
                "CLOUD_NAME": cloud_name,
                "API_KEY": api_key,
                "API_SECRET": api_secret,
            },
        )
        self.assertEqual(
            mock_settings.DEFAULT_FILE_STORAGE, "cloudinary_helper.storages.MediaStorage"
        )
        self.assertEqual(
            mock_settings.STATICFILES_STORAGE, "cloudinary_helper.storages.StaticStorage"
        )


if __name__ == "__main__":
    unittest.main()
