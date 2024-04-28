from djongo import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
    isUserMessage = models.BooleanField() 

    class Meta:
        abstract = True

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = {'message', 'isUserMessage'}

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=100)
    messages = models.ArrayField(model_container=Message, model_form_class=MessageForm)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['messages']
