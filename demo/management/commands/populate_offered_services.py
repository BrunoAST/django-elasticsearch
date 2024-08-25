from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from demo.models.expertise import Expertise
from demo.models.offered_service import OfferedService
from demo.models.service import Service
from demo.models.service_provider import ServiceProvider


fake = Faker()


class Command(BaseCommand):
    help = "Populate the database fake Service Provider Users"

    @transaction.atomic
    def handle(self, *args, **options):
        service_providers = ServiceProvider.objects.all()
        # expertise_count = Expertise.objects.count()
        service_count = Service.objects.count()
        
        for provider in service_providers:
            # Adds up to 5 offered services per provider
            for _ in range(0, 5):
                service = Service.objects.get(id=fake.random_int(1, service_count))
                
                offered_service = OfferedService(
                    description=fake.text(),
                    service_provider=provider,
                    service=service,
                )
                
                offered_service.full_clean()
                offered_service.save()
                
                expertises = Expertise.objects.filter(service=service)
                expertise_count = expertises.count()
                expertise = expertises[fake.random_int(0, expertise_count - 1)]
                
                if offered_service.expertises.filter(id=expertise.id).exists():
                    continue
                
                offered_service.expertises.add(expertise)
