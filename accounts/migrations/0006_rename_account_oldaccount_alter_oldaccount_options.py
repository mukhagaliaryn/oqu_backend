# Generated by Django 4.2.4 on 2024-08-12 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_specialty'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='OldAccount',
        ),
        migrations.AlterModelOptions(
            name='oldaccount',
            options={'verbose_name': 'Old Account', 'verbose_name_plural': 'Old Accounts'},
        ),
    ]
