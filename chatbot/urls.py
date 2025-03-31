from django.urls import path
from .views import chatbot_mock

urlpatterns = [
    path('talk/', chatbot_mock),
]
