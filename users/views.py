from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm

from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            role = form.cleaned_data.get("role")

            user = User.objects.get(username=username)

            Profile.objects.create(user=user, role=role)

            user_login = authenticate(username=username, password=password)
            login(request, user_login)

            messages.success(request, f"Account created for {username}!")

            if role == "LIBRARIAN":
                return redirect("library")
            else:
                return redirect("login")
    else:
        form = UserRegisterForm()

    return render(
        request, "../templates/registration/register.html", {"form": form}
    )
