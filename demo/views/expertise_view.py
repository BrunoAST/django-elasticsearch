from rest_framework import viewsets

from demo.models.expertise import Expertise
from demo.serializers.expertise_serializer import ExpertiseSerializer


class ExpertiseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpertiseSerializer
    queryset = Expertise.objects.all()
    