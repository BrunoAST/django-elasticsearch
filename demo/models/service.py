from django.db import models

from demo.models.category import Category


class Service(models.Model):
    name = models.CharField(max_length=100)
    # A service can be part of multiple categories
    # TODO: Add a ManyToManyField to ServiceCategory
    category = models.ForeignKey(
        Category, related_name="services", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"
