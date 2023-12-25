#Route logic are defined here

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CompanySerializer, EmployeeSerializer
from .models import TodoItem, Post, Company, Employee
from .forms import PostForm, RegisterForm
from rest_framework import viewsets

# Create your views here.
@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'home.html', {"posts": posts})


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


@login_required(login_url="/login")
#if user has no permission then raise error excep
@permission_required("myapp.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, "registration/signup.html", {"form": form})

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # this function will return all employees
    #of particular company by pk (primary key)
    # on companies/1/employees/ API/route/
    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emp, many=True, context={'request':request})
            return Response(emp_serializer.data)
        except:
            return Response({"message": "Invalid company pkey"})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer