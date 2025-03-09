from django.shortcuts import redirect
from rest_framework.views import APIView

from authentication.services.google_auth.google_sdk_login_flow_service import GoogleSdkLoginFlowService


class PublicApi(APIView):
    authentication_classes = []
    permission_classes = []
    

class GoogleLoginRedirectApi(PublicApi):
    def get(self, request, *args, **kwargs):
        google_login_flow = GoogleSdkLoginFlowService()

        authorization_url, state = google_login_flow.get_authorization_url()

        request.session["google_oauth2_state"] = state

        return redirect(authorization_url)
    