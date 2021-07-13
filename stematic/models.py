from django.db import models

# Create your models here.

class Stem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    users = models.IntegerField( blank =True)
    reviews = models.IntegerField( blank =True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank =True)
    teacher = models.CharField(max_length=20 )
    phototeacher = models.ImageField(upload_to='photo/%Y/%m/%d/', blank =True)
   


    def __str__(self):
        return self.title