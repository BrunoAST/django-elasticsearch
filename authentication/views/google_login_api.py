from django.contrib.auth import login
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from authentication.services.google_auth.google_sdk_login_flow_service import GoogleSdkLoginFlowService
from authentication.views.google_login_redirect_api import PublicApi
from demo.models.user import User


class GoogleLoginApi(PublicApi):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)
        state = serializers.CharField(required=False)
        
    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)
        
        code = input_serializer.validated_data.get('code')
        error = input_serializer.validated_data.get('error')
        state = input_serializer.validated_data.get('state')
        
        if error:
            return Response(
                {'error': error},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not code or not state:
            return Response(
                {'error': 'Code and state are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        session_state = request.session.get('google_oauth2_state')
        
        if session_state is None:
            return Response(
                {'error': 'CSRF check failed'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        del request.session['google_oauth2_state']
        
        if state != session_state:
            return Response(
                {'error': 'CSRF check failed'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        google_login_flow = GoogleSdkLoginFlowService()

        google_tokens = google_login_flow.get_tokens(code=code, state=state)

        id_token_decoded = google_tokens.decode_id_token()
        user_info = google_login_flow.get_user_info(google_tokens=google_tokens)

        user_email = id_token_decoded['email']
        user = User.objects.get(email=user_email)

        if user is None:
            return Response(
                {'error': f'User with email {user_email} is not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        login(request, user)

        result = {
            'id_token_decoded': id_token_decoded,
            'user_info': user_info,
        }

        return Response(result)
        
        