from django.db import models
from .courses import OldCourse
from main.models.users import CloneUser
from django.utils.translation import gettext_lazy as _


# Rating
class OldRating(models.Model):
    user = models.OneToOneField(CloneUser, on_delete=models.CASCADE, related_name='rating_user', verbose_name=_('User'))
    course = models.ForeignKey(OldCourse, on_delete=models.CASCADE, verbose_name=_('Course'))
    rating_score = models.PositiveSmallIntegerField(verbose_name=_('Score'), default=0)
    comment = models.TextField(verbose_name=_('Comment'), blank=True, null=True)

    def __str__(self):
        return '{}:{} - {}'.format(self.user, self.course, self.rating_score)

    class Meta:
        verbose_name = _('Old Rating')
        verbose_name_plural = _('Old Ratings')


# Subscribe
class OldSubscribe(models.Model):
    user = models.ForeignKey(CloneUser, on_delete=models.CASCADE, related_name='subscribe_user', verbose_name=_('User'))
    course = models.ForeignKey(OldCourse, on_delete=models.CASCADE, verbose_name=_('Course'))
    course_price = models.DecimalField(verbose_name=_('Course price'), max_digits=8, decimal_places=2)

    def __str__(self):
        return _('Subscribe: {}: {}').format(self.course, self.user)

    class Meta:
        verbose_name = _('Old Subscribe')
        verbose_name_plural = _('Old Subscribes')
