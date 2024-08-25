from django.urls import path, include
from rest_framework import routers

from demo.views.category_view import CategoryViewSet
from demo.views.expertise_view import ExpertiseViewSet
from demo.views.offered_services_view import OfferedServiceViewSet
from demo.views.service_provider_view import ServiceProviderViewSet
from demo.views.service_view import ServiceViewSet


router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"expertise", ExpertiseViewSet)
router.register(r"offered-service", OfferedServiceViewSet)
router.register(r"service-provider", ServiceProviderViewSet)
router.register(r"service", ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
