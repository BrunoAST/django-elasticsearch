from rest_framework import serializers

from demo.models import ServiceProvider


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = ServiceProvider.create_user(**validated_data)
        return user
