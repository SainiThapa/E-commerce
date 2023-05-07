from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def decide(request):
    return render(request,"interface.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")