from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, OldAccount


@receiver(post_save, sender=User)
def create_user_admin(sender, instance, created, **kwargs):
    if created:
        OldAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_admin(sender, instance, **kwargs):
    instance.account.save()
