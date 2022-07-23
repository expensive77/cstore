from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300, unique=True)
    email = models.CharField(max_length=400, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0, unique=True)
    picture=models.ImageField(null=True, blank=True, upload_to='media/profiles/', default='profiles/default_pp.png')
    postal_code = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    def __str__(self):
        return self.name


class EmailValidation(models.Model):
    code = models.IntegerField(unique=False)
    email = models.CharField(max_length=400, unique=True)
    def __str__(self):
        return self.email
