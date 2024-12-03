from django.apps import AppConfig

class CloudinaryHelperConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cloudinary_helper"

    def ready(self):
        # No need to replace FileField or ImageField classes here.
        pass
