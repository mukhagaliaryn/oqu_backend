# Generated by Django 4.2.4 on 2023-12-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centres', '0002_institution_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centres.direction', verbose_name='Направление'),
        ),
    ]
