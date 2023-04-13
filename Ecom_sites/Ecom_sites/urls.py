from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',include('Website.urls')),
    path('admin/', admin.site.urls),
    path('Index/', include('Website.urls')),
    path('hello/', include('Website.urls'))

]
