# Generated by Django 4.2.4 on 2024-01-19 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_course_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_headline',
        ),
    ]
