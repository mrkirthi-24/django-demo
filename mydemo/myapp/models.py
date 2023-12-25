#models in django are tables in database

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

class Post(models.Model):
    #Here on_delete states that if user is deleted then post also gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=50, choices = (('IT', 'IT'), ('Non-IT', 'Non-IT')))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    activity_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '-' + self.location

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=10, unique=True)
