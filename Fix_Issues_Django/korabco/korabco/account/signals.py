# Core Django imports.
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver


User = get_user_model()


# Saves username as email value
@receiver(pre_save, sender=User)
def save_username(sender, instance, *args, **kwargs):
    instance.username = instance.email