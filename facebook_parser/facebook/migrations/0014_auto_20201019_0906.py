# Generated by Django 3.1 on 2020-10-19 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0013_auto_20201013_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookchat',
            name='characters_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='gifs_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='links_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='messages_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='participants_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='photos_number',
        ),
        migrations.RemoveField(
            model_name='facebookchat',
            name='reactions_number',
        ),
    ]