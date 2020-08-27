# Generated by Django 3.1 on 2020-08-25 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_title', models.CharField(max_length=150)),
                ('gifs_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('facebook_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.facebookchat')),
            ],
        ),
    ]
