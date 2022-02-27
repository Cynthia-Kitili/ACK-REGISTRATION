from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='authentication/login.html'), name="login"),
]