from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
# Create your views here.
def home(request):
  return render(request, "authentication/index.html")

def register(request):
  if request.method== "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Hello {username}, You Have Been Succesfully Registered')
      return redirect ('home')
  else:
    form = UserRegisterForm()
  return render(request, "authentication/register.html",{'form':form})