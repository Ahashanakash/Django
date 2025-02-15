from django.db import models
from musician.models import Musician
from django.contrib.auth.models import User

# Create your models here.
class album(models.Model):
    Album_Name = models.CharField(max_length=50)
    Album_release_date = models.DateField()
    class Rating(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'
    rating = models.IntegerField(choices=Rating.choices,default=1)
    musician = models.ForeignKey(Musician, on_delete= models.CASCADE)

    def __str__(self):
        return self.Album_Name