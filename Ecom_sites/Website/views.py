from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html')

def Index(request):
    dest1= Destination()
    dest1.img='download.png'
    dests= [dest1,]
    return render(request,'Index.html',{'dests': dests})