from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from products.models import Course, Lesson, Chapter


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    specialty = models.CharField(verbose_name=_('Specialty'), max_length=32)
    about = models.TextField(verbose_name=_('About'), max_length=120, blank=True, null=True)
    favorite_courses = models.ManyToManyField(Course, blank=True, verbose_name=_('Favorite courses'))

    is_author = models.BooleanField(verbose_name=_('Author'), default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Headliner(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    subtitle = models.TextField(verbose_name=_('Subtitle'), blank=True, null=True)
    poster = models.ImageField(verbose_name=_('Poster'), upload_to='products/headliners/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Headliner')
        verbose_name_plural = _('Headliners')


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
        return '{}: {}'.format(self.user.full_name, self.chapter.title)

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
