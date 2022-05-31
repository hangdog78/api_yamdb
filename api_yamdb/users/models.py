from django.contrib.auth.models import AbstractUser
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

class User(AbstractUser):
  role = models.PositiveSmallIntegerField(
    choices=ROLE_CHOICES,
    null=False
    )
  