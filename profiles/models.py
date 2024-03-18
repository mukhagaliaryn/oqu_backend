from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from products.models import Course, Lesson, Chapter


# User course
# ----------------------------------------------------------------------------------------------------------------------
class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user.full_name, self.course.name)

    class Meta:
        verbose_name = _('User course')
        verbose_name_plural = _('User courses')


# User chapter
# ----------------------------------------------------------------------------------------------------------------------
class UserChapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user.full_name, self.chapter.chapter_name)

    class Meta:
        verbose_name = _('User chapter')
        verbose_name_plural = _('User chapters')


# User lesson
# ----------------------------------------------------------------------------------------------------------------------
class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    is_completed = models.BooleanField(verbose_name=_('Is_completed'), default=False)

    def __str__(self):
        return '{}: {}'.format(self.user.full_name, self.lesson.title)

    class Meta:
        verbose_name = _('User lesson')
        verbose_name_plural = _('User lessons')
