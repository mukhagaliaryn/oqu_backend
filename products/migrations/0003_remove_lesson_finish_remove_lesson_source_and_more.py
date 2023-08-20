# Generated by Django 4.2.4 on 2023-08-12 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_lesson_duration_lesson_finish_lesson_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='finish',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='source',
        ),
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Уровень'),
        ),
    ]
