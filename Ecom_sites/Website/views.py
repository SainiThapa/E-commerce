from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html')

def index(request):
    return render(request,'Index.html')