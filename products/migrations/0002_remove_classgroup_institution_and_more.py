# Generated by Django 4.2.4 on 2023-12-04 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classgroup',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='classgroup',
            name='students',
        ),
        migrations.RemoveField(
            model_name='classgroup',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='classgroup',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='owner',
        ),
        migrations.DeleteModel(
            name='ClassGroup',
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
    ]
