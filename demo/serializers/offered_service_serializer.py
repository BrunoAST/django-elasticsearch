from rest_framework import serializers

from demo.models.offered_service import OfferedService
from demo.serializers.expertise_serializer import ExpertiseSerializer
from demo.serializers.service_provider_serializer import ServiceProviderSerializer
from demo.serializers.service_serializer import ServiceSerializer


class OfferedServiceSerializer(serializers.ModelSerializer):
    service_provider = ServiceProviderSerializer()
    service = ServiceSerializer()
    expertises = ExpertiseSerializer(many=True)
    
    class Meta:
        model = OfferedService
        fields = '__all__'
        