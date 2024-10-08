from django.db import models

from demo.models.service import Service


class Expertise(models.Model):
    name = models.CharField(max_length=100)
    service = models.ForeignKey(
        Service,
        related_name='expertise',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
    