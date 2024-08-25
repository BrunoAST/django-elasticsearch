from rest_framework import viewsets

from demo.models.offered_service import OfferedService
from demo.serializers.offered_service_serializer import OfferedServiceSerializer


class OfferedServiceViewSet(viewsets.ModelViewSet):
    serializer_class = OfferedServiceSerializer
    queryset = OfferedService.objects.all()
    