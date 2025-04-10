from .views import AidObjects
from django.urls import path

urlpatterns = [
    path('aid/', AidObjects, name='Aidobjects')
]
