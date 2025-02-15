# Generated by Django 5.1.5 on 2025-02-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=12)),
                ('Instrument_Type', models.CharField(max_length=50)),
            ],
        ),
    ]
