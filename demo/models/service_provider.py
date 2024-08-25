from django.db import models

from demo.choices.cpf_cnpj import CNPJ_CNPJ_CHOICES

from .base_user import BaseUser


class ServiceProvider(BaseUser):
    work_type = models.CharField(choices=CNPJ_CNPJ_CHOICES)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    # TODO: Add Slug Field for URL
    