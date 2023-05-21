from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'homepage1.html')

def hello(request):
    return render(request,"home.html")
def product(request):
    dests=Destination.objects.all()
    return render(request,"product.html",{'dests':dests})

def contact(request):
    return render(request,'Contact.html')
def index(request):
    return render(request,"homepage.html")
def buy(request):
    return render(request,"Buy.html")
def categories(request):
    return render(request,"categories.html")