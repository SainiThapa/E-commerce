from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Destination
# from .models import Cartobject
from django.contrib import messages


# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request,'Slider.html')
    dests=Destination.objects.all()
    return render(request,"Slider.html",{'dests':dests})

def hello(request):
    return render(request,"home.html")
def product(request):
    dests=Destination.objects.all()
    return render(request,"product.html",{'dests':dests})
def singleProduct(request, num=None):
    data = Destination.objects.get(num=num)
    return render(request, "product_detail.html",{"data":data})

def payment(request):
    return render(request,'payment.html')

def contact(request):
    return render(request,'Contact.html')
def index(request):
    return render(request,"homepage.html")
def buy(request):
    return render(request,"Buy.html")
def categories(request):
    return render(request,"categories.html")


def slider(request):
    dests=Destination.objects.all()
    return render(request,"Slider.html",{'dests':dests})

def albums(request, num=None):
    data=Destination.objects.all()
    return render(request,"albums.html",{"data":data})

def lightstick(request):
    data = Destination.objects.all()
    return render(request,"lightstick.html",{"data":data})

def fashion(request):
    data = Destination.objects.all()
    return render(request,"fashion.html",{"data":data})


def mycart(request, num=None):
    data=Destination.objects.get(num=num)
    # print("Product number is "+ str(data.num))
    
    return render(request,"Mycart.html",{"data":data})