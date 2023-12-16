from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("home/", views.home, name="homepage"), 
    path("todos/", views.todos, name="todos"), 
    path("signup/", views.signup, name="signup"),
]