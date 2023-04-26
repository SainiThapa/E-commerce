from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('Website.urls')),
    path('home/',include('Website.urls')),
    path('admin/', admin.site.urls),
    path('index/', include('Website.urls')),
    path('hello/', include('Website.urls')),
    path('contact/', include('Website.urls')),
    path('product/', include('Website.urls')),
]
# urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
