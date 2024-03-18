# Generated by Django 4.2.4 on 2024-03-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_lesson_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('EXPRESS', 'Express'), ('DETAIL', 'Detailed'), ('DIRECT', 'Directed')], default='Express', max_length=40, verbose_name='Type'),
        ),
    ]
