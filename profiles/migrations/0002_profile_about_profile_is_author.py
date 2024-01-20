# Generated by Django 4.2.4 on 2024-01-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Author'),
        ),
    ]