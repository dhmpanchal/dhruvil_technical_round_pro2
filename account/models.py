from django.contrib.auth.models import AbstractUser
from django.db import models
from account.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
