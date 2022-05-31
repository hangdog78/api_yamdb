from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.conf import settings

from .validators import UsernameValidator


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
    
    username_validator = UsernameValidator
    username = models.CharField(
        'User name',
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField('Email', max_length=254, unique=True)
    
    
    def __str__(self):
        return str(self.username)
    
