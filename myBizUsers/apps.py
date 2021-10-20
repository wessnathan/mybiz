from django.apps import AppConfig


class MybizusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myBizUsers'
    
    def ready(self):
        import myBizUsers.signals