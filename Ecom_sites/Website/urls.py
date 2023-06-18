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
    path('paymentmethod',views.payment,name="payment"),
    path('product_detail/<num>/',views.singleProduct, name="num"),
    path('slider',views.slider, name="slider"),
    path('albums',views.albums, name="albums"),

    path('lightsticks',views.lightstick, name="lightstick"),

    path('fashion&merch',views.fashion, name="fashion"),
    path('mycart/<num>/',views.mycart, name="mycart"),


]