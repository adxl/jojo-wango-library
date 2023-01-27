from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import models
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm

from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
                
            user = authenticate(username=username, password=password)
            
            if form.cleaned_data.get('role') == 'yes':
                # Here is the problem , I want to update the role field in the userprofile model
                
                user_profile = UserProfile.objects.get(user=user)
                user_profile.role = 'librairy'
                user_profile.save()
                
            
                
            
            login(request, user)

            messages.success(request, f'Account created for {username}!')
        
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, '../templates/registration/register.html' , {'form': form})
