from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


# Category
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_('Key'), max_length=255, unique=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='products/category/',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Topic(models.Model):
    own = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_('Key'), max_length=255, unique=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='products/topics/',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')


# Course model
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Language
class Language(models.Model):
    name = models.CharField(verbose_name=_('Language name'), max_length=64)
    slug = models.SlugField(verbose_name=_('Language key'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


# Course
class Course(models.Model):
    COURSE_TYPE = (
        ('DETAIL', _('Detailed')),
        ('DIRECT', _('Directed')),
    )
    name = models.CharField(verbose_name=_('Title'), max_length=40)
    course_type = models.CharField(verbose_name=_('Type'), max_length=40,
                                   choices=COURSE_TYPE, default=COURSE_TYPE[0][1])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    topic = models.ForeignKey(Topic, related_name='topic', on_delete=models.CASCADE,
                              verbose_name=_('Topic'))
    poster = models.ImageField(verbose_name=_('Poster'), upload_to='products/poster/',
                               blank=True, null=True)
    about = models.TextField(verbose_name=_('About'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    ln = models.ManyToManyField(Language, verbose_name=_('Language'), blank=True)
    authors = models.ManyToManyField(User, verbose_name=_('Authors'),
                                     related_name="authors", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    requirements = models.ManyToManyField('Course', verbose_name=_('Requirements'), blank=True)

    all_rating = models.DecimalField(verbose_name=_('All rating'), max_digits=3, decimal_places=2, default=0)

    # for headline slides
    is_headline = models.BooleanField(verbose_name=_('Headline'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ('-date_created', )


# Rating
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    rating_score = models.PositiveSmallIntegerField(verbose_name=_('Score'), default=0)

    def __str__(self):
        return f'{self.user}:{self.course} - {self.rating_score}'

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')


# Purpose
class Purpose(models.Model):
    product = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    item = models.TextField(verbose_name=_('What will you learn'), null=True, blank=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = _('Purpose')
        verbose_name_plural = _('Purposes')


# Chapter
class Chapter(models.Model):
    product = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    chapter_name = models.CharField(verbose_name=_('Chapter name'), max_length=64)
    about = models.TextField(verbose_name=_('About'), blank=True, null=True)

    def __str__(self):
        return self.chapter_name

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')


# Lesson
class Lesson(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))
    access = models.BooleanField(verbose_name=_('Access'), default=True)

    date_created = models.DateTimeField(verbose_name=_('Date created'), auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)
    view = models.PositiveIntegerField(verbose_name=_('View'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


# Video
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    frame_url = models.CharField(verbose_name=_('iFrame URL'), max_length=255)
    duration = models.PositiveSmallIntegerField(verbose_name=_('Duration (min)'), default=0)

    def __str__(self):
        return self.lesson

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')


# Article
class Article(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    duration = models.PositiveSmallIntegerField(verbose_name=_('Duration (min)'), default=0)

    def __str__(self):
        return self.lesson

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
