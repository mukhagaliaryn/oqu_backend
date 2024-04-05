from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from .courses import Course, Lesson, Chapter


# UserCourse
# ----------------------------------------------------------------------------------------------------------------------
class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_course', verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.course.name)

    class Meta:
        verbose_name = _('User course')
        verbose_name_plural = _('User courses')


# UserChapter
# ----------------------------------------------------------------------------------------------------------------------
class UserChapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chapter', verbose_name=_('User'))
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, verbose_name=_('User course'))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.chapter)

    class Meta:
        verbose_name = _('User chapter')
        verbose_name_plural = _('User chapters')


# UserLesson
# ----------------------------------------------------------------------------------------------------------------------
class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lesson', verbose_name=_('User'))
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, verbose_name=_('User course'))
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.lesson)

    class Meta:
        verbose_name = _('User lesson')
        verbose_name_plural = _('User lessons')
