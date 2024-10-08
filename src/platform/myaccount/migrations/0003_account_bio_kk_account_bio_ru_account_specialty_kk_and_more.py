# Generated by Django 4.2.4 on 2024-08-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio_kk',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='account',
            name='bio_ru',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='account',
            name='specialty_kk',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Specialty'),
        ),
        migrations.AddField(
            model_name='account',
            name='specialty_ru',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Specialty'),
        ),
    ]
