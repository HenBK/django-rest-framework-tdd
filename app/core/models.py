from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user and returns it"""

        if email is None:
            raise ValueError(
                'The email address is mandatory when creating a new user'
            )

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        superuser = self.create_user(email, password=password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save()

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email and not username"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
