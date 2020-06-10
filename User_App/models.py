from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Information(AbstractBaseUser):
    # id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=32)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email