from attrs import define
from django.core.exceptions import ImproperlyConfigured

from project.env import env


@define
class GoogleSdkLoginCredentials:
    client_id: str
    client_secret: str
    project_id: str
    

def google_sdk_get_login_credentials() -> GoogleSdkLoginCredentials:
    client_id = env('DJANGO_GOOGLE_OUATH2_CLIENT_ID', default='')
    client_secret = env('DJANGO_GOOGLE_OAUTH2_CLIENT_SECRET', default='')
    project_id = env('DJANGO_GOOGLE_OAUTH2_PROJECT_ID', default='')

    if not client_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_ID missing in env.")

    if not client_secret:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_SECRET missing in env.")

    if not project_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_PROJECT_ID missing in env.")

    credentials = GoogleSdkLoginCredentials(
        client_id=client_id,
        client_secret=client_secret, 
        project_id=project_id
    )

    return credentials
