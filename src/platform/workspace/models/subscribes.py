from django.db import models
from django.utils.translation import gettext_lazy as _
from src.platform.myaccount.models import User
from src.platform.resources.models import Course


# Subscribe
class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribe_user', verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    course_price = models.DecimalField(verbose_name=_('Course price'), max_digits=8, decimal_places=2)

    def __str__(self):
        return _('Subscribe: {}: {}').format(self.course, self.user)

    class Meta:
        verbose_name = _('Subscribe')
        verbose_name_plural = _('Subscribes')
