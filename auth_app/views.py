from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "auth_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                response = redirect("dashboard")  # Redirect to task dashboard
                response.set_cookie("access", str(refresh.access_token), httponly=True)
                response.set_cookie("refresh", str(refresh), httponly=True)

                return response
            else:
                messages.error(request, "Invalid username or password.")
    
    else:
        form = LoginForm()
    
    return render(request, "auth_app/login.html", {"form": form})

@login_required
def logout_view(request):
    response = redirect("login")
    response.delete_cookie("access")
    response.delete_cookie("refresh")
    logout(request)
    return response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task  # Import Task model

@login_required
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user)  # Get tasks for the logged-in user
    return render(request, "auth_app/dashboard.html", {"tasks": tasks})
