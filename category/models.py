from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=True)
    slug = models.SlugField()

    def get_url(self):
        return reverse('blog_by_category', args=[self.slug])


    # to rename your categorys on your database to categories 
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name    