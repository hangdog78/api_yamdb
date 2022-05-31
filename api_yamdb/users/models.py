from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

USER = 1
MODERATOR = 2
ADMIN = 3
SUPERUSER = 4

ROLE_CHOICES = (
          (USER, 'user'),
          (MODERATOR, 'moderator'),
          (ADMIN, 'admin'),
          (SUPERUSER, 'superuser'),
      )


class CustomUserManager(BaseUserManager):
  
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email,
                          is_staff=True,
                          is_superuser=True,
                          role = SUPERUSER,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user
      

class User(AbstractUser):
  role = models.PositiveSmallIntegerField(
    choices=ROLE_CHOICES,
    null=False,
    verbose_name='User role',
    help_text='User role'
    )
 
  objects = CustomUserManager()