from django.contrib import admin
from .models import TodoItem, Post

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Post)