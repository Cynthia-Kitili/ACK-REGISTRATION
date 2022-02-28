from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home,name="home"),
    path('home', views.home,name="home"),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('register/', views.register, name='register'),
    path('leader', views.leader, name='leader'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='authentication/logout.html'), name="logout"),
    
]

urlpatterns += staticfiles_urlpatterns()