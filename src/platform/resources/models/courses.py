from django.db import models
from django.utils.translation import gettext_lazy as _
from src.platform.myaccount.models import User


# Category
# ----------------------------------------------------------------------------------------------------------------------
# Category
class Category(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    slug = models.SlugField(_('Key'), max_length=128)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('order', )


# SubCategory
class Subcategory(models.Model):
    own = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='sub_categories', verbose_name=_('Category')
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.SlugField(_('Key'), max_length=128)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')
        ordering = ('order', )


# Course
# ----------------------------------------------------------------------------------------------------------------------
# Language
class Language(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Key'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


# Course
class Course(models.Model):
    COURSE_TYPE = (
        ('FREE', _('Free')),
        ('PRO', _('Pro')),
    )

    name = models.CharField(_('Name'), max_length=128)
    category = models.ForeignKey(
        Category, related_name='courses',
        on_delete=models.CASCADE, verbose_name=_('Category')
    )
    sub_category = models.ForeignKey(
        Subcategory, related_name='sub_courses',
        on_delete=models.CASCADE, verbose_name=_('Subcategory')
    )
    course_type = models.CharField(_('Course type'), max_length=32, choices=COURSE_TYPE, default='FREE')
    price = models.DecimalField(verbose_name=_('Price'), max_digits=8, decimal_places=2, default=0)
    poster = models.ImageField(_('Poster'), upload_to='platform/resources/courses/', blank=True, null=True)
    about = models.TextField(_('About'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    ln = models.ManyToManyField(Language, verbose_name=_('Languages'), blank=True)
    authors = models.ManyToManyField(
        User, verbose_name=_('Authors'),
        related_name="author_courses", blank=True
    )
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    last_update = models.DateField(_('Last update'), auto_now=True)
    rating = models.DecimalField(_('Rating'), max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ('-date_created', )


# Purpose
class Purpose(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='purposes', verbose_name=_('Course')
    )
    item = models.TextField(_('What will you learn'), null=True, blank=True)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = _('Purpose')
        verbose_name_plural = _('Purposes')
        ordering = ('order', )


# Rating
class Rating(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='user_ratings', verbose_name=_('User')
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='course_ratings', verbose_name=_('Course')
    )
    assessment = models.PositiveSmallIntegerField(_('Assessment'), default=0)
    comment = models.TextField(_('Comment'), blank=True, null=True)

    def __str__(self):
        return '{}:{} - {}'.format(self.user, self.course, self.assessment)

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')


# Chapter
class Chapter(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='chapters', verbose_name=_('Course')
    )
    name = models.CharField(_('Name'), max_length=128)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        ordering = ('order', )


# Lesson
class Lesson(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='course_lessons', verbose_name=_('Course')
    )
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE,
        related_name='chapter_lessons', verbose_name=_('Chapter')
    )
    about = models.TextField(_('About'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    last_update = models.DateTimeField(_('Last update'), auto_now=True)
    duration = models.PositiveSmallIntegerField(_('Duration (min)'), default=0)
    access = models.BooleanField(_('Access'), default=False)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ('order', )
