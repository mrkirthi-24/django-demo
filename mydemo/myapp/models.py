from django.db import models
from django.contrib.auth.models import User

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
