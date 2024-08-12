# Generated by Django 4.2.4 on 2024-08-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0010_alter_oldaccount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloneuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='clone_user_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='cloneuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='cloneuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='clone_user_set', to='auth.permission'),
        ),
    ]