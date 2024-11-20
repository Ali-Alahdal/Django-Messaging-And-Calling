import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)
    email = models.CharField(max_length=225, unique=True)
    username = models.CharField(max_length=225 , unique=True)











  