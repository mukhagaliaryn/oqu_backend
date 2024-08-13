from django.db import models
from django.utils.translation import gettext_lazy as _
from src.platform.myaccount.models import User


# Account
# ----------------------------------------------------------------------------------------------------------------------
class Account(models.Model):
    ACCOUNT_TYPE = (
        ('STUDENT', _('Student')),
        ('AUTHOR', _('Author')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    account_type = models.CharField(
        _('Account type'), max_length=64,
        choices=ACCOUNT_TYPE, default=ACCOUNT_TYPE[0][1]
    )
    specialty = models.CharField(_('Specialty'), max_length=128, blank=True, null=True)
    bio = models.TextField(_('Bio'), max_length=256, blank=True, null=True)
    account_fill = models.BooleanField(_('Is filled out'), default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
