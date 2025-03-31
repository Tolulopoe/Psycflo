from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot_mock(request):
    user_message = request.data.get('message', '')

    return Response({
        "reply": f"You said: '{user_message}'. This is a mock reply from the chatbot."
    })


