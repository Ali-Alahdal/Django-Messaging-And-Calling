import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Unique related name to prevent clashes
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set_permissions',  # Ensure this is unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )