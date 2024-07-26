from django.apps import AppConfig


class TiendastresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tiendastres'

    def ready(self):
        from . import signals
