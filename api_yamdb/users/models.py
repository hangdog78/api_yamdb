from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.conf import settings


class User(AbstractUser):
    
    bio = models.TextField(
        'Биография',
        blank=True,
    ) 
    role = models.CharField(
        choices=settings.ROLE_CHOICES,
        max_length=20,
        blank=False,
        verbose_name='User role',
        help_text='Describes users permissions',
        default=settings.ROLES['user']
        )
    