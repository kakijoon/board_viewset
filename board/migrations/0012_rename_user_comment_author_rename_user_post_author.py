# Generated by Django 4.0.3 on 2022-03-24 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_comment_user_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
