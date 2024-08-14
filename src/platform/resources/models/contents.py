from django.db import models
from django.utils.translation import gettext_lazy as _
from src.platform.resources.models.courses import Course, Lesson


# Video
class Video(models.Model):
    TYPE_VIDEO_URL = (
        ('YOUTUBE', _('YouTube')),
        ('VIMEO', _('Vimeo')),
    )

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='course_video', verbose_name=_('Course')
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        related_name='lesson_video', verbose_name=_('Lesson')
    )
    url_type = models.CharField(_('URL type'), max_length=64, choices=TYPE_VIDEO_URL, default='YOUTUBE')
    url = models.CharField(_('URL'), max_length=256)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return _('Video: {}').format(self.lesson)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        ordering = ('order', )
