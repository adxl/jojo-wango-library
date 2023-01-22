from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            login(request, user)

            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, '../templates/registration/register.html' , {'form': form})
