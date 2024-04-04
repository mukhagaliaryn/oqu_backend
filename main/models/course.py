from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


# Category
# ----------------------------------------------------------------------------------------------------------------------
# Category
class Category(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_('Key'), max_length=255, unique=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='main/course/categories/',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


# SubCategory
class SubCategory(models.Model):
    own = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_('Key'), max_length=255, unique=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='main/course/subcategories/',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


# Course
# ----------------------------------------------------------------------------------------------------------------------
# Language
class Language(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=64)
    slug = models.SlugField(verbose_name=_('Key'), max_length=64)

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

    name = models.CharField(verbose_name=_('Title'), max_length=40)
    course_type = models.CharField(verbose_name=_('Course type'), max_length=40,
                                   choices=COURSE_TYPE, default=COURSE_TYPE[0][1])
    course_price = models.DecimalField(verbose_name=_('Course price'), max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    sub_category = models.ForeignKey(SubCategory, related_name='sub_category', on_delete=models.CASCADE,
                                     verbose_name=_('Subcategory'))
    poster = models.ImageField(verbose_name=_('Poster'), upload_to='main/course/posters/',
                               blank=True, null=True)
    about = models.TextField(verbose_name=_('About'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    ln = models.ManyToManyField(Language, verbose_name=_('Languages'), blank=True)
    course_authors = models.ManyToManyField(User, verbose_name=_('Authors'),
                                            related_name="course_authors", blank=True)
    date_created = models.DateTimeField(verbose_name=_('Date created'), auto_now_add=True)
    last_update = models.DateField(verbose_name=_('Last update'), auto_now=True)
    all_rating = models.DecimalField(verbose_name=_('All rating'), max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ('-date_created', )


# Purpose
class Purpose(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    item = models.TextField(verbose_name=_('What will you learn'), null=True, blank=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = _('Purpose')
        verbose_name_plural = _('Purposes')


# Chapter
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    index = models.PositiveSmallIntegerField(verbose_name=_('Index'), default=1)
    name = models.CharField(verbose_name=_('Chapter name'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')


# Lesson
# ----------------------------------------------------------------------------------------------------------------------
# Lesson
class Lesson(models.Model):
    LESSON_TYPE = (
        ('VIDEO', _('Video')),
        ('ARTICLE', _('Article')),
    )

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    index = models.PositiveSmallIntegerField(verbose_name=_('Index'), default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))

    lesson_type = models.CharField(verbose_name=_('Lesson type'), max_length=40,
                                   choices=LESSON_TYPE, default=LESSON_TYPE[0][1])
    access = models.BooleanField(verbose_name=_('Access'), default=False)
    date_created = models.DateTimeField(verbose_name=_('Date created'), auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)
    duration = models.PositiveSmallIntegerField(verbose_name=_('Duration (min)'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


# Video
class Video(models.Model):
    URL_TYPE = (
        ('YOUTUBE', _('YouTube')),
        ('VIMEO', _('Vimeo')),
        ('KINESCOPE', _('Kinescope')),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    url_type = models.CharField(verbose_name=_('URL type'), max_length=40,
                                choices=URL_TYPE, default=URL_TYPE[0][1])
    frame_url = models.CharField(verbose_name=_('iFrame URL'), max_length=255)

    def __str__(self):
        return 'Видео: {}'.format(self.lesson)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')


# Article
class Article(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

    def __str__(self):
        return 'Статья: {}'.format(self.lesson)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
