# Generated by Django 4.2.4 on 2023-12-04 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=64, verbose_name='Название раздела')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О разделе')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Направление')),
                ('slug', models.SlugField(max_length=64, verbose_name='Ключ направления')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовка')),
                ('access', models.BooleanField(default=True, verbose_name='Доступ')),
                ('level', models.PositiveSmallIntegerField(default=100, verbose_name='Уровень')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Длительность (мин)')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='Просмотров')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.chapter', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('SUBJECT', 'Школьный предмет'), ('COURSE', 'Курс')], default='Школьный предмет', max_length=255, verbose_name='Тип продукта')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='products/poster/', verbose_name='Обложка')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О продукте')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('authors', models.ManyToManyField(blank=True, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Авторы')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название видео')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание видео')),
                ('frame_url', models.CharField(max_length=255, verbose_name='iFrame ссылка')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Длительность (мин)')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видеохостинг',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовка')),
                ('task_type', models.CharField(choices=[('WRITE', 'Материальные задачи'), ('QUIZ', 'Тест')], default='Материальные задачи', max_length=255, verbose_name='Тип задачи')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Задание')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Длительность (мин)')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Вопрос')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Тело вопроса')),
                ('format', models.CharField(choices=[('ONE', 'Одновариантный'), ('MULTI', 'Многовариантный')], default='Одновариантный', max_length=64, verbose_name='Формат')),
                ('solution', models.TextField(blank=True, null=True, verbose_name='Решение')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.task', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(blank=True, null=True, verbose_name='Цель обучение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Цель')),
            ],
            options={
                'verbose_name': 'Цель обучение',
                'verbose_name_plural': 'Цели обучения',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='accounts/institution/images/', verbose_name='Изображение')),
                ('date_created', models.DateField(verbose_name='Год основания')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='Веб-сайт')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Основатель')),
            ],
            options={
                'verbose_name': 'Учреждение',
                'verbose_name_plural': 'Учреждения',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=64, null=True, verbose_name='Название')),
                ('item', models.CharField(blank=True, max_length=64, null=True, verbose_name='Значение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Особенности')),
            ],
            options={
                'verbose_name': 'Особенность',
                'verbose_name_plural': 'Особенности',
            },
        ),
        migrations.CreateModel(
            name='ClassGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('flow', models.CharField(choices=[('NOT_DEFINED', 'Не выбрано'), ('ONE', 1), ('TWO', 2), ('THREE', 3)], default='Не выбрано', verbose_name='Поток')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.institution', verbose_name='Учереждение')),
                ('students', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Ученики')),
                ('subjects', models.ManyToManyField(blank=True, to='products.product', verbose_name='Программы')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='Руководитель')),
            ],
            options={
                'verbose_name': 'Класс/Группа',
                'verbose_name_plural': 'Классы/Группы',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Раздел'),
        ),
        migrations.CreateModel(
            name='BaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Ключ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/category/', verbose_name='Изображение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.basecategory', verbose_name='Супер категория')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Ответ')),
                ('correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категорий',
                'ordering': ('name',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.basecategory',),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ('category__name', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.category',),
        ),
        migrations.AddField(
            model_name='product',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='products.topic', verbose_name='Тема'),
        ),
    ]
