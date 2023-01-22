from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='../templates/registration/login.html'), name='login'),
    path('register/', auth_views.LoginView.as_view(template_name='../templates/registration/register.html'), name='register'),
]
