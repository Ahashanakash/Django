# Generated by Django 5.1.5 on 2025-02-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Album_release_date',
            field=models.DateTimeField(),
        ),
    ]
