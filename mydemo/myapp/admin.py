from django.contrib import admin
from .models import TodoItem, Post

# Register your models here to view and alter then in django admin.
admin.site.register(TodoItem)
admin.site.register(Post)