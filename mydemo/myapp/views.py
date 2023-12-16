from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from .models import TodoItem, Post
from .forms import PostForm, RegisterForm

# Create your views here.
@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


@login_required(login_url="/login")
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