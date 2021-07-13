from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank =True)
    location = models.CharField(max_length=20 )
    date = models.DateTimeField(default=datetime.now, blank=True)
   
   


    def __str__(self):
        return self.title
