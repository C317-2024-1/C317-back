from djongo import models
from django import forms
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
    
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=100)
    messages = models.JSONField(default=[])
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
