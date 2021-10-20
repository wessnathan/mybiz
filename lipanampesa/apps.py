from django.apps import AppConfig


class LipanampesaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lipanampesa'
    
    def ready(self):
        import lipanampesa.signals