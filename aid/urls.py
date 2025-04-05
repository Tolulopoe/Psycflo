from django.urls import path
from .views import dummy_aid_view  # replace this with real view later

urlpatterns = [
    path('', dummy_aid_view, name='aid-home'),
]
