# Generated by Django 4.2.4 on 2023-09-23 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_classgroup_flow_alter_classgroup_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classgroup',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='Руководитель'),
        ),
    ]