<<<<<<< HEAD
from .views import AidObjects
from django.urls import path

urlpatterns = [
    path('aid/', AidObjects, name='Aidobjects')
=======
from django.urls import path
from .views import AidRequestCreateView, AidRequestListView

urlpatterns = [
    path('', AidRequestListView.as_view(), name='aid-list'),
    path('create/', AidRequestCreateView.as_view(), name='aid-create'),
    path('list/', AidRequestListView.as_view(), name='aid-list'),
>>>>>>> aid-endpoint
]
