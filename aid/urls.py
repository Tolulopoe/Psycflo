from .views import Aid_objects
from django.urls import path

urlpatterns={
    path('aid/',Aid_objects, name='Aidobjects')
}