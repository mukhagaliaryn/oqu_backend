# Generated by Django 4.2.4 on 2024-01-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_course_is_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='all_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Score'),
        ),
    ]
