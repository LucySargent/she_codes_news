from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser): #inherit django's AbstractUser resource
    pass

    def __str__(self):
        return self.username  #to print the username nicely!


