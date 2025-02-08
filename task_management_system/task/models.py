from django.db import models
from catagory.models import Catagory

# Create your models here.
class TaskModel (models.Model):
    title = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField()
    Category_Name = models.ManyToManyField(Catagory)
    
    def __str__(self):
        return self.title