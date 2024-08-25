from rest_framework import serializers

from demo.models.expertise import Expertise
from demo.serializers.service_serializer import ServiceSerializer


class ExpertiseSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    
    class Meta:
        model = Expertise
        fields = '__all__'
        