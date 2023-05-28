from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('index',views.index,name='index'),
    path('hello',views.hello,name='hello'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
    path('buy',views.buy,name='buy'),
    path('categories',views.categories,name="buy"),
    path('product_detail/<name>/',views.singleProduct, name="name")
]