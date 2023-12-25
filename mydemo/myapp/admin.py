from django.contrib import admin
from .models import TodoItem, Post, Employee, Company

# Register your models here to view and alter then in django admin.
admin.site.register(TodoItem)
admin.site.register(Post)
admin.site.register(Company)
admin.site.register(Employee)