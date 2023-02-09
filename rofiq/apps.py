from django.apps import AppConfig


class RofiqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rofiq'
    
    def ready(self):
        import rofiq.signals
