# Generated by Django 4.2.4 on 2023-09-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_alter_userchapter_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquizdata',
            name='max_score',
            field=models.PositiveSmallIntegerField(default=60, verbose_name='Максимальный балл'),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='max_score',
            field=models.PositiveSmallIntegerField(default=30, verbose_name='Максимальный балл'),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='status',
            field=models.CharField(choices=[('START', 'Старт'), ('PROGRESS', 'В процессе'), ('FINISH', 'Завершено')], default='Старт', max_length=255, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='max_score',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='Максимальный балл'),
        ),
    ]