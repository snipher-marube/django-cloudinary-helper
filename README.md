# Django Cloudinary Helper

This package helps Django developers easily configure Cloudinary for serving static and media files. It automatically detects the development or production environment based on the `DEBUG` setting.

## Features

- Automatically detects `DEBUG` mode.
- Configures Cloudinary for media and static files in production.
- Falls back to local storage in development.

## Installation

To install the package, run:

```bash
pip install django-cloudinary-helper
```

## Usage

1. Add `cloudinary_helper` to your `INSTALLED_APPS`:
   In your `settings.py`, add `cloudinary_helper` to the `INSTALLED_APPS` list:

```python
    INSTALLED_APPS = [
        ...
        'cloudinary_helper',
        ...
    ]
```


2. Add storage configurations for static and media files:
    To ensure your static and media files are served via Cloudinary in production, add the following settings to your `settings.py`:
    
    ```python
    from decouple import config 
    from cloudinary_helper.utils import setup_cloudinary
    if DEBUG:
        # Development
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [BASE_DIR / 'static']
        STATIC_ROOT = BASE_DIR / 'staticfiles' # This is where collectstatic will store static files
        MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'static/media' # This is where media files will be stored
        DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
        STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    else:
        # Production
        STATIC_URL = '/static/'
        MEDIA_URL = '/media/'
        setup_cloudinary(
            config('CLOUDINARY_CLOUD_NAME'),
            config('CLOUDINARY_API_KEY'),
            config('CLOUDINARY_API_SECRET')
        )
     

        DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.CloudinaryMediaStorage'
        STATICFILES_STORAGE = 'cloudinary_helper.storages.CloudinaryStaticStorage'

    ```
    

3. (Optional) Using the storage in your app:
    With the above configurations, your `FileField` and `ImageField` fields in Django models will automatically use Cloudinary for file uploads in production. In development, when `DEBUG = True`, local file storage will be used instead.

### Automatic Field Swapping

The package dynamically replaces the `FileField` and `ImageField` with `CloudinaryField` when `DEBUG = False`. 

This means you don't need to manually adjust your models. Simply use the default `FileField` and `ImageField` in your models, and the package will handle the rest:

```python
from django.db import models
from cloudinary_helper.storages import get_storage_class

class YourModel(models.Model):
    image = models.ImageField(storage=get_storage_class(), upload_to='images/')
    file = models.FileField(storage=get_storage_class(), upload_to='files/')

```


### Advantages of This Approach

1. **Ease of Use**:
   Developers don’t need to learn or remember to use `CloudinaryField` explicitly in their models.

2. **Seamless Integration**:
   The behavior changes dynamically based on the environment (`DEBUG` setting).

3. **Backward Compatibility**:
   Models written with standard Django fields will still work as expected without modifications.

---

This implementation makes your package more developer-friendly by abstracting away unnecessary details while providing seamless integration with both development and production environments.



4. (Optional) Handling Static Files:
    In production, Cloudinary will automatically serve your static files. In development, the `StaticStorage` class will fall back to the local file system. No additional configuration is required for static files other than the `STATICFILES_STORAGE`

## Notes

 - In production (when `DEBUG = False`), Cloudinary will be used for both static and media files.
 - In development (when `DEBUG = True`), local file storage will be used for both static and media files.
 - The `setup_cloudinary()` function can be helpful for setting up the storage automatically without needing to manually configure it in `settings.py`.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure all changes are well tested and follow Django's best practices.

## License

This package is open-source and available under the MIT License. Feel free to use it in your projects.



