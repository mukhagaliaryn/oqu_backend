# Generated by Django 4.2.4 on 2024-03-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_userchapter_options_alter_usercourse_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite_courses',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Headliner',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]