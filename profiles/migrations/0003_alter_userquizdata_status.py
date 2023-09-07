# Generated by Django 4.2.4 on 2023-09-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userquizdata_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquizdata',
            name='status',
            field=models.CharField(choices=[('START', 'Старт'), ('PROGRESS', 'В процессе'), ('FINISH', 'Завершено')], default='Старт', max_length=255, verbose_name='Статус'),
        ),
    ]
