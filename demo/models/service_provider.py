from django.db import models

from demo.choices.cpf_cnpj import CNPJ_CNPJ_CHOICES
from demo.choices.user_roles import UserRole
from .user import User


class ServiceProvider(User):
    work_type = models.CharField(choices=CNPJ_CNPJ_CHOICES, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)

    @classmethod
    def create_user(cls, **kwargs):
        user = cls.objects.create_user(**kwargs)
        user.role = UserRole.SERVICE_PROVIDER.value
        user.save()
        return user

    def save(self, *args, **kwargs):
        self.role = UserRole.SERVICE_PROVIDER.value
        super().save(*args, **kwargs)


