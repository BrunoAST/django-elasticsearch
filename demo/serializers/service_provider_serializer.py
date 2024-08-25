from rest_framework import serializers

from demo.models.service_provider import ServiceProvider


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = (
            "id",
            "full_name",
            "email",
            "cellphone",
            "username",
            "work_type",
            "cnpj",
            "cpf",
        )
        