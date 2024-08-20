# Generated by Django 4.2.4 on 2024-08-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='name_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='course',
            name='about_en',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='course',
            name='about_kk',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='course',
            name='about_ru',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='about_en',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='about_kk',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='about_ru',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='purpose',
            name='item_en',
            field=models.TextField(blank=True, null=True, verbose_name='What will you learn'),
        ),
        migrations.AddField(
            model_name='purpose',
            name='item_kk',
            field=models.TextField(blank=True, null=True, verbose_name='What will you learn'),
        ),
        migrations.AddField(
            model_name='purpose',
            name='item_ru',
            field=models.TextField(blank=True, null=True, verbose_name='What will you learn'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
    ]