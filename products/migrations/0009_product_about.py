# Generated by Django 4.2.4 on 2023-08-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_purpose_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='О продукте'),
        ),
    ]
