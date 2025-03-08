from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views.customer_registration_view import CustomerRegistrationView
from authentication.views.login_view import LoginView
from authentication.views.service_provider_profile_view import ServiceProviderProfileView
from authentication.views.service_provider_registration_view import ServiceProviderRegistrationView


urlpatterns = [
    path(
        'service-provider-registration/',
        ServiceProviderRegistrationView.as_view(),
        name='service-provider-registration'
    ),
    path(
        'customer-registration/',
        CustomerRegistrationView.as_view(),
        name='customer-registration'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'service-provider-profile/',
        ServiceProviderProfileView.as_view(),
        name='service-provider-profile'
    )
]
