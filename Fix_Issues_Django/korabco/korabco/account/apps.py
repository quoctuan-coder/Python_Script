from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    # Starts signals to create author profile.
    def ready(self):
        from . import signals
