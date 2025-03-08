from rest_framework.permissions import BasePermission

from demo.choices.user_roles import UserRole


class IsCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        return request.user.role == UserRole.CUSTOMER.value
    