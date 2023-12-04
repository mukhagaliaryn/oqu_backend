from django.db import models
from accounts.models import User


# Category
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class BaseCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Ключ', max_length=255, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='products/category/',
                              blank=True, null=True)
    category = models.ForeignKey('BaseCategory', on_delete=models.PROTECT,
                                 null=True, blank=True, verbose_name='Супер категория')


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__isnull=True)


class Category(BaseCategory):
    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class TopicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__isnull=False)


class Topic(Category):
    objects = TopicManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('category__name', 'name', )
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


# Main product (subjects, courses, ...) models
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# Product
class Product(models.Model):
    PRODUCT_CHOICE = (
        ('SUBJECT', 'Школьный предмет'),
        ('COURSE', 'Курс'),
    )

    product_type = models.CharField(verbose_name='Тип продукта', max_length=255,
                                    choices=PRODUCT_CHOICE, default=PRODUCT_CHOICE[0][1])
    name = models.CharField(verbose_name='Название', max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    topic = models.ForeignKey(Topic, related_name='topic', on_delete=models.CASCADE,
                              verbose_name='Тема')
    poster = models.ImageField(verbose_name='Обложка', upload_to='products/poster/',
                               blank=True, null=True)
    about = models.TextField(verbose_name='О продукте', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    authors = models.ManyToManyField(User, verbose_name='Авторы',
                                     related_name="authors", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Purpose
class Purpose(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Цель')
    item = models.TextField(verbose_name='Цель обучение', null=True, blank=True)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Цель обучение'
        verbose_name_plural = 'Цели обучения'


# Features
class Feature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Особенности')
    label = models.CharField(verbose_name='Название', max_length=64, null=True, blank=True)
    item = models.CharField(verbose_name='Значение', max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.label}: {self.item}'

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'


# Chapter
class Chapter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Раздел')
    chapter_name = models.CharField(verbose_name='Название раздела', max_length=64)
    about = models.TextField(verbose_name='О разделе', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.chapter_name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


# Lesson
# ------------------------------------------------------------------------------------------------
class Lesson(models.Model):
    title = models.CharField(verbose_name='Заголовка', max_length=255)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Раздел')
    access = models.BooleanField(verbose_name='Доступ', default=True)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень', default=100)
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность (мин)', default=0)

    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name='Последнее обновление', auto_now=True)
    view = models.PositiveIntegerField(verbose_name='Просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


# Video
class Video(models.Model):
    title = models.CharField(verbose_name='Название видео', max_length=64)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')

    description = models.TextField(verbose_name='Описание видео', blank=True, null=True)
    frame_url = models.CharField(verbose_name='iFrame ссылка', max_length=255)
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность (мин)', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видеохостинг'


# Tasks
class Task(models.Model):
    TASK_CHOICE = (
        ('WRITE', 'Материальные задачи'),
        ('QUIZ', 'Тест'),
    )
    title = models.CharField(verbose_name='Заголовка', max_length=255)
    task_type = models.CharField(verbose_name='Тип задачи', max_length=255,
                                 choices=TASK_CHOICE, default=TASK_CHOICE[0][1])
    body = models.TextField(verbose_name='Задание', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность (мин)', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задачи'


# Quiz
class Question(models.Model):

    FORMAT = (
        ('ONE', 'Одновариантный'),
        ('MULTI', 'Многовариантный'),
    )

    title = models.CharField(verbose_name='Вопрос', blank=False, null=False)
    body = models.TextField(verbose_name='Тело вопроса', blank=True, null=True)
    format = models.CharField(verbose_name='Формат', choices=FORMAT, default=FORMAT[0][1], max_length=64)
    solution = models.TextField(verbose_name='Решение', blank=True, null=True)
    quiz = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')

    def __str__(self):
        return self.title

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


# Answers (4B1, 8Bn)
class Answer(models.Model):
    text = models.TextField(verbose_name='Ответ', blank=False, null=False)
    correct = models.BooleanField(verbose_name='Правильный ответ', default=False)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
