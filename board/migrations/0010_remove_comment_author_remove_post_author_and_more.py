# Generated by Django 4.0.3 on 2022-03-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
