from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(default='', max_length=15)
    address = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)