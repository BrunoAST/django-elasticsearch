from django.db import models

from demo.choices.user_roles import UserRole


class BaseUser(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()
    cellphone = models.CharField(max_length=11, unique=True)
    profile_photo = models.ImageField(upload_to="users/profile/%Y/%m/%d/", null=True, blank=True)
    username = models.SlugField(unique=True)
    role = models.CharField(
        choices=UserRole.choices(),
        default=UserRole.SERVICE_PROVIDER.value
    )

    class Meta:
        """
        Abstract base classes are useful when you want to put some common information into a
        number of other models. You write your base class and put abstract=True in the Meta class. 
        This model will then not be used to create any database table. Instead, when it is used
        as a base class for other models, its fields will be added to those of the child class.
        """
        abstract = True

    def __str__(self):
        return f"{self.full_name} - {self.email}"
