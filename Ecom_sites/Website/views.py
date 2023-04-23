from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'homepage1.html')

def hello(request):
    return render(request,"home.html")
def index(request):
    dest1=Destination()
    dest1.name="WINNER EXIT-E 2016"
    dest1.img="WINNER2.jpg"
    dest1.offer=True
    dest1.price=3400

    dest2=Destination()
    dest2.name="iKON CONTINUE 2018"
    dest2.img="iKON1.jpeg"
    dest2.offer=False
    dest2.price=3500
    dests=[dest1,dest2,]
    return render(request,"homepage.html",{'dests':dests})
    
def contact(request):
    return render(request,'Contact.html')

def product(request):
    dest1=Destination()
    dest1.name="EXIT-E"
    dest1.img="WINNER2.jpg"
    dest1.offer=True
    dest1.price=3400

    dest2=Destination()
    dest2.name="CONTINUE"
    dest2.img="iKON1.jpeg"
    dest2.offer=False
    dest2.price=3500
    dests=[dest1,dest2,]
    return render(request,"product.html",{'dests':dests})