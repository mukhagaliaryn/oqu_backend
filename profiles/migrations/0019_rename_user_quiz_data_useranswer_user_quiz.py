# Generated by Django 4.2.4 on 2023-09-12 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_alter_useranswer_answers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='user_quiz_data',
            new_name='user_quiz',
        ),
    ]
