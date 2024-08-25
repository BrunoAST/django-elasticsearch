from django.core.management.base import BaseCommand
from django.db.models import Q
from faker import Faker
from demo.models.service_provider import ServiceProvider


fake = Faker()


class Command(BaseCommand):
    help = "Populate the database fake Service Provider Users"

    def handle(self, *args, **options):
        for _ in range(50_000):
            username = fake.user_name()
            email = fake.email()

            if not ServiceProvider.objects.filter(
                Q(username=username) | Q(email=email)
            ).exists():
                ServiceProvider.objects.create(
                    full_name=fake.name(),
                    email=email,
                    password=fake.password(),
                    cellphone=f"{fake.random_number(11)}",
                    username=username,
                    work_type=fake.random_element(elements=("PF", "PJ")),
                    cnpj=f"{fake.random_number(14)}",
                    cpf=f"{fake.random_number(11)}",
                )
