# Generated by Django 5.0.3 on 2024-12-19 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Songs', '0002_song_lyrics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
    ]
