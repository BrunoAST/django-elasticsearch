from django.core.management.base import BaseCommand, CommandError
import json
from demo.models.service import Service
from demo.models.expertise import Expertise
from demo.models.category import Category


class Command(BaseCommand):
    help = 'Populate the database with services data'
    
    def handle(self, *args, **options):
        """
        Steps:
        1. Create all the Category objects (if they don't already exist)
        2. Create all the Service objects (if they don't already exist)
        3. Create all the Expertise objects (if they don't already exist)
        """

        file = self._load_data("demo/data/services.json")
        
        for data in file["data"]:
            self._create_category(data)
            self._create_service(data)
            self._create_expertise(data)

    def _load_data(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise CommandError('File does not exist.')
        except json.JSONDecodeError:
            raise CommandError('Failed to decode JSON.')
        except Exception as e:
            raise CommandError(f'An error occurred: {str(e)}')

    def _create_category(self, data):
        category = data["category"]

        if not Category.objects.filter(name=category).exists():
            Category.objects.create(name=category)

    def _create_service(self, data):
        service_name = data["service"]
        category_name = data["category"]
        category = Category.objects.get(name=category_name)

        if not Service.objects.filter(
            name=service_name, category_id=category.pk
        ).exists():
            service = Service.objects.create(name=service_name, category=category)
            service.save()

    def _create_expertise(self, data):
        expertises = data["expertises"]
        service_name = data["service"]
        service = Service.objects.get(name=service_name)

        for expertise in expertises:
            if not Expertise.objects.filter(
                name=expertise, service_id=service.pk
            ).exists():
                Expertise.objects.create(name=expertise, service=service)
