from django.contrib import admin
from .models import TodoItem, Post, Employee, Company

# Register your models here to view and alter then in django admin.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
 
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    list_filter = ('company',)

admin.site.register(TodoItem)
admin.site.register(Post)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)