from time import sleep

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username




