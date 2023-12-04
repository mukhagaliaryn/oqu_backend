from django.db import models
from accounts.models import User
from products.models import Product


# Create your models here.
# Institution model
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class Direction(models.Model):
    name = models.CharField(verbose_name='Направление', max_length=64)
    slug = models.SlugField(verbose_name='Ключ направления', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Institution(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='accounts/institution/images/', blank=True, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Направление')
    date_created = models.DateField(verbose_name='Год основания', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True, blank=True, null=True)
    website = models.URLField(verbose_name='Веб-сайт', max_length=255, blank=True, null=True)
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Основатель')
    # ...

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждения'


# Class/Group model
# -----------------------------------------------------------------------------------------------
class ClassGroup(models.Model):
    FLOW_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('ONE', 1),
        ('TWO', 2),
        ('THREE', 3),
    )

    name = models.CharField(verbose_name='Название', max_length=255)
    flow = models.CharField(verbose_name='Поток',
                            choices=FLOW_CHOICE, default=FLOW_CHOICE[0][1])
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name='Учереждение')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='teacher',
                                blank=True, null=True, verbose_name='Руководитель')
    students = models.ManyToManyField(User, blank=True, verbose_name='Ученики')
    subjects = models.ManyToManyField(Product, blank=True, verbose_name='Программы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс/Группа'
        verbose_name_plural = 'Классы/Группы'
