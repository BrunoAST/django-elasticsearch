from django.db import models

from demo.choices.user_roles import UserRole
from .user import User


class Customer(User):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    @classmethod
    def create_user(cls, **kwargs):
        user = cls.objects.create_user(**kwargs)
        user.role = UserRole.CUSTOMER.value
        user.save()
        return user

    def save(self, *args, **kwargs):
        self.role = UserRole.CUSTOMER.value
        super().save(*args, **kwargs)
