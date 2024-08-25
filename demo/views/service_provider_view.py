from rest_framework import viewsets

from demo.models.service_provider import ServiceProvider
from demo.serializers.service_provider_serializer import ServiceProviderSerializer


class ServiceProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    