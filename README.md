# Django Cloudinary Helper

This package helps Django developers easily configure Cloudinary for serving static and media files. It automatically detects the development or production environment based on the `DEBUG` setting.

## Features

- Automatically detects `DEBUG` mode.
- Configures Cloudinary for media and static files in production.
- Falls back to local storage in development.

## Installation

```bash
pip install django-cloudinary-helper
```

## Usage

Add `cloudinary_helper` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'cloudinary_helper',
    ...
]
```

Add the following settings to your `settings.py`:

```python
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY: 'your_api_key',
    'API_SECRET: 'your_api_secret',
}
```

Add the following to your `urls.py`:

