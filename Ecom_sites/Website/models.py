from django.db import models

# Create your models here.
class Destination(models.Model):
    num =  models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    categories = models.CharField(max_length=100)
    
    