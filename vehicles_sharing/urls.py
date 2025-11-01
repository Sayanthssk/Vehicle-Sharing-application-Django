from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AdminApp/', include('AdminApp.urls')),
    path('Api/', include('UserApp.urls')),
    path('OwnerApp/', include('OwnerApp.urls')),
    path('', include('vehicleapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)