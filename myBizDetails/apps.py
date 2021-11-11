from django.apps import AppConfig


class MybizdetailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myBizDetails'
    
    def ready(self):
        import myBizDetails.signals
