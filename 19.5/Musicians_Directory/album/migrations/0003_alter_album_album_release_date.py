# Generated by Django 5.1.5 on 2025-02-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Album_release_date',
            field=models.DateField(),
        ),
    ]
