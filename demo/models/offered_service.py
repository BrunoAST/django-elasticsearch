from django.db import models

from .service import Service
from .service_provider import ServiceProvider


class OfferedService(models.Model):
    description = models.CharField(max_length=600)
    service_provider = models.ForeignKey(
        ServiceProvider, related_name="offered_services", on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        related_name='offered_services',
        on_delete=models.CASCADE,
    )
    expertises = models.ManyToManyField(
        'Expertise',
        related_name='offered_services',
    )

    def __str__(self) -> str:
        return f"{self.service_provider.full_name}"
