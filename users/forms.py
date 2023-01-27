from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    
    labelAttr = "block mb-2 text-sm font-medium text-gray-900 dark:text-white"
    inputAttr = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    selectAttr = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email Address')
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput)
    username = forms.CharField(required=True, label='Username')
    role = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Are you a librairy?')
    
    
    first_name.widget.attrs.update({'class': inputAttr})
    last_name.widget.attrs.update({'class': inputAttr})
    email.widget.attrs.update({'class': inputAttr})
    password1.widget.attrs.update({'class': inputAttr})
    password2.widget.attrs.update({'class': inputAttr})
    username.widget.attrs.update({'class': inputAttr})
    role.widget.attrs.update({'class': selectAttr})
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        
        
        
