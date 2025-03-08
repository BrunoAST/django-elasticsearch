from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

from demo.choices.user_roles import UserRole
from demo.models.customer import Customer
from demo.models.service_provider import ServiceProvider


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == UserRole.SERVICE_PROVIDER.value:
                concrete_user = ServiceProvider.objects.get(pk=user.id)
                
            if user.role == UserRole.CUSTOMER.value:
                concrete_user = Customer.objects.get(pk=user.id)
            
            refresh = RefreshToken.for_user(concrete_user)
            
            refresh['role'] = concrete_user.role
            refresh['username'] = concrete_user.username
            refresh['user_id'] = concrete_user.pk

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
