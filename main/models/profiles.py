from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from .courses import OldCourse, OldLesson, OldChapter


# UserCourse
# ----------------------------------------------------------------------------------------------------------------------
class OldUserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_course', verbose_name=_('User'))
    course = models.ForeignKey(OldCourse, on_delete=models.CASCADE, verbose_name=_('Course'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.course.name)

    class Meta:
        verbose_name = _('Old User course')
        verbose_name_plural = _('Old User courses')


# UserChapter
# ----------------------------------------------------------------------------------------------------------------------
class OldUserChapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chapter', verbose_name=_('User'))
    user_course = models.ForeignKey(OldUserCourse, on_delete=models.CASCADE, verbose_name=_('User course'))
    chapter = models.ForeignKey(OldChapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.chapter)

    class Meta:
        verbose_name = _('Old User chapter')
        verbose_name_plural = _('Old User chapters')


# UserLesson
# ----------------------------------------------------------------------------------------------------------------------
class OldUserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lesson', verbose_name=_('User'))
    user_course = models.ForeignKey(OldUserCourse, on_delete=models.CASCADE, verbose_name=_('User course'))
    lesson = models.ForeignKey(OldLesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.lesson)

    class Meta:
        verbose_name = _('Old User lesson')
        verbose_name_plural = _('Old User lessons')
        ordering = ('lesson__index', )
