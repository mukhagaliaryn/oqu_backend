# Generated by Django 4.2.4 on 2024-03-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_lesson_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='about',
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapter_index',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Chapter index'),
        ),
    ]