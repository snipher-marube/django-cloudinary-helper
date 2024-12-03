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
2. Add Cloudinary configuration to your `settings.py`:
   You will need to configure Cloudinary by adding the following settings to your `settings.py`:

   ```python
      CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'your_cloud_name',
        'API_KEY': 'your_api_key',
        'API_SECRET': 'your_api_secret',
        'SECURE': True,
        }
    ```

3. Optional: Call `setup_cloudinary()` in `settings.py`:
    To configure Cloudinary in your Django app, you can call the `setup_cloudinary()` function. This is optional, but it helps simplify the configuration by setting the appropriate storage for both static and media files:

    ```python
    from cloudinary_helper.utils import setup_cloudinary

    # Set up Cloudinary storage with your Cloudinary credentials
    setup_cloudinary('your_cloud_name', 'your_api_key', 'your_api_secret')
    ```

4. Add storage configurations for static and media files:
    To ensure your static and media files are served via Cloudinary in production, add the following settings to your `settings.py`:
    
    ```python
    DEFAULT_FILE_STORAGE = 'cloudinary_helper.storages.MediaStorage'
    STATICFILES_STORAGE = 'cloudinary_helper.storages.StaticStorage'
    ```
    

5. (Optional) Using the storage in your app:
    With the above configurations, your `FileField` and `ImageField` fields in Django models will automatically use Cloudinary for file uploads in production. In development, when `DEBUG = True`, local file storage will be used instead.

### Automatic Field Swapping

The package dynamically replaces the `FileField` and `ImageField` with `CloudinaryField` when `DEBUG = False`. 

This means you don't need to manually adjust your models. Simply use the default `FileField` and `ImageField` in your models, and the package will handle the rest:

```python
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
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



6. (Optional) Handling Static Files:
    In production, Cloudinary will automatically serve your static files. In development, the `StaticStorage` class will fall back to the local file system. No additional configuration is required for static files other than the `STATICFILES_STORAGE`

## Notes

 - In production (when `DEBUG = False`), Cloudinary will be used for both static and media files.
 - In development (when `DEBUG = True`), local file storage will be used for both static and media files.
 - The `setup_cloudinary()` function can be helpful for setting up the storage automatically without needing to manually configure it in `settings.py`.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure all changes are well tested and follow Django's best practices.

## License

This package is open-source and available under the MIT License. Feel free to use it in your projects.



