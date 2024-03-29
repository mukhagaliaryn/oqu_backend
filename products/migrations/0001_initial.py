# Generated by Django 4.2.4 on 2024-01-16 06:38

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Key')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/category/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=64, verbose_name='Chapter name')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Title')),
                ('course_type', models.CharField(choices=[('DETAIL', 'Detailed'), ('DIRECT', 'Directed')], default='Detailed', max_length=40, verbose_name='Type')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='products/poster/', verbose_name='Poster')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('last_update', models.DateField(auto_now=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Authors')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Language name')),
                ('slug', models.SlugField(max_length=64, verbose_name='Language key')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('access', models.BooleanField(default=True, verbose_name='Access')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Duration')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='View')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.chapter', verbose_name='Chapter')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_url', models.CharField(max_length=255, verbose_name='iFrame URL')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Duration (min)')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lesson', verbose_name='Lesson')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Key')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/topics/', verbose_name='Image')),
                ('own', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_score', models.PositiveSmallIntegerField(default=0, verbose_name='Score')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(blank=True, null=True, verbose_name='What will you learn')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Purpose',
                'verbose_name_plural': 'Purposes',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='ln',
            field=models.ManyToManyField(blank=True, to='products.language', verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='course',
            name='requirements',
            field=models.ManyToManyField(blank=True, to='products.course', verbose_name='Requirements'),
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='products.topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Course'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lesson', verbose_name='Lesson')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
