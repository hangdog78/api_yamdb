from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email,
                          is_staff=True,
                          is_superuser=True,
                          role = settings.SUPERUSER,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user
      

class User(AbstractUser):
    
    role = models.PositiveSmallIntegerField(
        choices=settings.ROLE_CHOICES,
        null=False,
        verbose_name='User role',
        help_text='User role'
        )
    objects = CustomUserManager()