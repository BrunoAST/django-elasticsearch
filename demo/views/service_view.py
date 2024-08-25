from rest_framework import viewsets

from demo.models.service import Service
from demo.serializers.service_serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    