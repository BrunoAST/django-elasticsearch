from enum import Enum


class UserRole(Enum):
    SERVICE_PROVIDER = "service_provider"
    CUSTOMER = "customer"

    @classmethod
    def choices(cls):
        return [(role.value, role.value.replace("_", " ").title())
                for role in cls]
