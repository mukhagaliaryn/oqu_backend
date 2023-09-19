# Generated by Django 4.2.4 on 2023-09-16 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_alter_userproduct_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='status',
            field=models.CharField(choices=[('START', 'Старт'), ('PROGRESS', 'В процессе'), ('CONFIRM', 'Получение оценку'), ('FINISH', 'Завершено')], default='Старт', max_length=255, verbose_name='Статус'),
        ),
    ]