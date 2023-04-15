from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'homepage.html')

def hello(request):
    return render(request,"home.html")
def Index(request):
    return render(request,'Index.html')
def contact(request):
    return render(request,'Contact.html')