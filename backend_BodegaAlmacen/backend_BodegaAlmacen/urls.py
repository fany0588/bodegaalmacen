from django.contrib import admin
from django.urls import path, include
from app_BodegaAlmacen import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('app_BodegaAlmacen.urls')),
]
