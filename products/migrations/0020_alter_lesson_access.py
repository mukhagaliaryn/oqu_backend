# Generated by Django 4.2.4 on 2024-03-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_course_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='access',
            field=models.BooleanField(default=False, verbose_name='Access'),
        ),
    ]
