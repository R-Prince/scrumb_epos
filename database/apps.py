from django.apps import AppConfig


class DatabaseConfig(AppConfig):
    name = 'Database'

    def ready(self):
        import database.signals


class DatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'database'
