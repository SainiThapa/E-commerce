from django.db import models

# Create your models here.
class Destination:
    name : str
    price : float
    img: str
    offer: bool
    
    