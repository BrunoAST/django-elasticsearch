from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.permissions.is_service_provider_permission import IsServiceProviderPermission


class ServiceProviderProfileView(APIView):
    permission_classes = [IsAuthenticated, IsServiceProviderPermission]
    
    def get(self, request):
        return Response('Service Provider Profile')    
    