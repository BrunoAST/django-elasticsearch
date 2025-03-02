from django.db import models

from demo.choices.user_roles import UserRole
from .base_user import BaseUser


class Customer(BaseUser):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def save(self, *args, **kwargs):
        self.role = UserRole.CUSTOMER.value
        super().save(*args, **kwargs)
