# Generated by Django 4.2.4 on 2024-02-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('VIDEO', 'Video'), ('ARTICLE', 'Article')], default='Video', max_length=40, verbose_name='Lesson type'),
        ),
    ]
