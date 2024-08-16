from django.db import models
from django.utils.translation import gettext_lazy as _
from src.platform.myaccount.models import User
from src.platform.resources.models import Course, Lesson, Chapter


# UserCourse
# ----------------------------------------------------------------------------------------------------------------------
class UserCourse(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='u_user_courses', verbose_name=_('User')
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='c_user_courses', verbose_name=_('Course')
    )
    current_lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name=_('Current lesson')
    )
    is_completed = models.BooleanField(_('Is_completed'), default=False)
    completion_percentage = models.FloatField(_('Completion percentage'), default=0.0)

    def __str__(self):
        return '{}: {}'.format(self.user, self.course.name)

    class Meta:
        verbose_name = _('User course')
        verbose_name_plural = _('User courses')


# UserChapter
# ----------------------------------------------------------------------------------------------------------------------
class UserChapter(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='u_user_chapters', verbose_name=_('User')
    )
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE,
        related_name='ch_user_chapters', verbose_name=_('Chapter')
    )
    user_course = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE,
        related_name='uc_user_chapters', verbose_name=_('User course')
    )
    is_completed = models.BooleanField(_('Is_completed'), default=False)
    completion_percentage = models.FloatField(_('Completion percentage'), default=0.0)

    def __str__(self):
        return '{}: {}'.format(self.user, self.chapter)

    class Meta:
        verbose_name = _('User chapter')
        verbose_name_plural = _('User chapters')


# UserLesson
# ----------------------------------------------------------------------------------------------------------------------
class UserLesson(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='u_user_lessons', verbose_name=_('User')
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        related_name='l_user_lessons', verbose_name=_('Lesson')
    )
    user_course = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE,
        related_name='uc_user_lessons', verbose_name=_('User course')
    )
    current_position = models.PositiveIntegerField(_('Current position'), default=0)
    is_started = models.BooleanField(_('Is started'), default=False)
    is_completed = models.BooleanField(_('Is_completed'), default=False)
    start_date = models.DateTimeField(_('Start date'), null=True, blank=True)
    completion_date = models.DateTimeField(_('Completion date'), null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.user, self.lesson)

    class Meta:
        verbose_name = _('User lesson')
        verbose_name_plural = _('User lessons')
        ordering = ('lesson__order', )
