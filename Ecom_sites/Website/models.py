from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Destination(models.Model):
    num =  models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    categories = models.CharField(max_length=100)

class Cart(models.Model):
    id =  models.UUIDField(default=uuid.uuid4, primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

class CartItem(models.Model):
    product = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name=  "items")
    cart =  models.ForeignKey(Cart,on_delete=models.CASCADE, related_name="Cart_items")
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.product)