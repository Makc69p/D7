from django.apps import AppConfig


class MD2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'M_D1'
class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'

    def ready(self):
        from . import signals