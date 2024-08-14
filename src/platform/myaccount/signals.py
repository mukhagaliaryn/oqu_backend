from django.db.models.signals import post_save
from django.dispatch import receiver
from src.platform.myaccount.models.users import User
from src.platform.myaccount.models.accounts import Account


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
    instance.account.save()
