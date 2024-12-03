import unittest
from django.conf import settings
from cloudinary_helper.storages import StaticStorage, MediaStorage

class StorageTests(unittest.TestCase):
    def test_debug_static_storage(self):
        settings.DEBUG = True
        storage = StaticStorage()
        self.assertIn("django.core.files.storage.FileSystemStorage", str(type(storage)))

    def test_production_static_storage(self):
        settings.DEBUG = False
        storage = StaticStorage()
        self.assertIn("storages.backends.cloudinary.CloudinaryStorage", str(type(storage)))
