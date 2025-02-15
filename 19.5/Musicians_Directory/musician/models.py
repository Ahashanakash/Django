from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_number= models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"