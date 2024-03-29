# Generated by Django 4.2.4 on 2024-02-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_lesson_lesson_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url_type',
            field=models.CharField(choices=[('YOUTUBE', 'YouTube'), ('VIMEO', 'Vimeo'), ('KINESCOPE', 'Kinescope')], default='YouTube', max_length=40, verbose_name='URL type'),
        ),
    ]
