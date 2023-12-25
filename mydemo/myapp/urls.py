#all the routes are defined here

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path("", views.home, name="home"), 
    path("home/", views.home, name="homepage"), 
    path("todos/", views.todos, name="todos"), 
    path("signup/", views.signup, name="signup"),
    path("createpost/", views.create_post, name="create_post"),
    path("api/", include(router.urls))
]