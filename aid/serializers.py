from rest_framework import serializers
from .models import AidRequest

class AidRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidRequest
        fields = '__all__'
