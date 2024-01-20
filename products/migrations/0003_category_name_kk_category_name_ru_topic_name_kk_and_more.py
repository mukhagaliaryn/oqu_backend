# Generated by Django 4.2.4 on 2024-01-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_lesson_duration_article_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
    ]