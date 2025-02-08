from django.db import models

# Create your models here.
class Musician(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_number= models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name