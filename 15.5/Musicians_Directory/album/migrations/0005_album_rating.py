# Generated by Django 5.1.5 on 2025-02-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_remove_album_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
