# Generated by Django 4.2.4 on 2023-08-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_language_options_language_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='school_view',
            field=models.CharField(choices=[('NOT_DEFINED', 'Не выбрано'), ('GENERAL', 'Общеобразовательная'), ('LYCEUM', 'Лицей')], default='Не выбрано', max_length=255, verbose_name='Вид'),
        ),
    ]
