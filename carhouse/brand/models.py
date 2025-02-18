from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    Brand_Name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    def __str__(self):
        return f"{self.Brand_Name}"