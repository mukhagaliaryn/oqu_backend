from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from products.models import Course


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    about = models.TextField(verbose_name=_('About'), max_length=120, blank=True, null=True)
    favorite_courses = models.ManyToManyField(Course, blank=True, verbose_name=_('Favorite courses'))

    is_author = models.BooleanField(verbose_name=_('Author'), default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
