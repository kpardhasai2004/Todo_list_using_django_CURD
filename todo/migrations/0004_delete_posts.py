# Generated by Django 4.0.4 on 2022-08-01 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_title_posts_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='posts',
        ),
    ]
