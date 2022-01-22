from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=10, null=False, unique=True)
    age = models.IntegerField(default=18)

