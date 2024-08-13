from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MyAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.platform.myaccount'
    verbose_name = _('Platform | My account')
