from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from typing import Union
from django.contrib import messages
# Create your views here.
def decide(request):
    return render(request,"interface.html")
def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname',"default value")
        lastname=request.POST.get('lastname','default value')
        username=request.POST.get('username','default value')
        email=request.POST.get('email','default value')
        password1=request.POST.get('password1','default value')
        password2=request.POST.get('password2','default value')
        
        if (password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already in use')
                return redirect('register')
            else:
                            user=User.objects.create_user(username=username,password=password1, email=email,firstname=firstname,lastname=lastname)
                            user.save()
                            print('USER CREATED !')
                            return redirect('login')
        else:
            messages.info(request,"Password doesnot match")
            return redirect('register')
    else:
        return render(request,"register.html")

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password1']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')