from django.urls import path
from . import views

urlpatterns=[
    path('decide',views.decide,name='decide'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    ]