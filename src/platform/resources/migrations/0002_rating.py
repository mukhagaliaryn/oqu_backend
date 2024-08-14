# Generated by Django 4.2.4 on 2024-08-14 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.PositiveSmallIntegerField(default=0, verbose_name='Assessment')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_ratings', to='resources.course', verbose_name='Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
