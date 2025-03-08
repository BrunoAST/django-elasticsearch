from django.contrib.auth.models import AbstractUser, models, Group, Permission

from demo.choices.user_roles import UserRole


class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("service_provider", "Service Provider"),
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="demo_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="demo_user_set",
        related_query_name="user",
    )

    role = models.CharField(
        choices=UserRole.choices(), default=UserRole.SERVICE_PROVIDER.value
    )

    cellphone = models.CharField(max_length=11, null=True, blank=True)
