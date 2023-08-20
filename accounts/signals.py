from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Account
from profiles.models import Profile


@receiver(post_save, sender=User)
def create_user_admin(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_admin(sender, instance, **kwargs):
    instance.account.save()
    instance.profile.save()
