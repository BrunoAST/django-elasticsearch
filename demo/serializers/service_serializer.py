from rest_framework import serializers

from demo.models.service import Service
from demo.serializers.category_serializer import CategorySerializer


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Service
        fields = '__all__'
        