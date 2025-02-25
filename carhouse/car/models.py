from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    Car_name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='carname/media/uploads/', blank=True, null=True)
    purchased_by = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.Car_name
    
class Comment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name = 'comments')
    name = models.CharField(max_length=100)
    email=models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
    
