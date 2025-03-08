from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers.service_provider_serializer import ServiceProviderSerializer


class ServiceProviderRegistrationView(APIView):
    def post(self, request):
        serializer = ServiceProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
