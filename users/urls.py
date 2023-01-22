from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='../templates/registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    
]
