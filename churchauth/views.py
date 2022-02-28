from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm, LeadersForm
from django.contrib.auth.decorators import login_required
import requests
from .models import LeadersModel
# Create your views here.


def home(request):
  leader= LeadersModel.objects.all()
  return render(request, "authentication/index.html",{'leader':leader})

def leader(request):
    if request.method == "POST":
        form = LeadersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = LeadersForm()
    return render(request, 'authentication/leaders.html', {'form': form})
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

def edit(request, id):
    leader= LeadersModel.objects.get(id=id)
    return render(request, 'authentication/edit.html', {'leader': leader})

def update(request, id):
    leader= LeadersModel.objects.get(id=id)
    form = LeadersForm(request.POST, instance = leader)
    if form.is_valid():
        form.save()
        return redirect("/home")
    return render(request, 'authentication/edit.html', {'leader': leader})


def destroy(request,id):
    leader= LeadersModel.objects.get(id=id)
    leader.delete()
    return redirect("/home")

@login_required()
def profile(request):
  response=requests.get('https://type.fit/api/quotes').json()
  
  return render(request, 'authentication/profile.html', {'response':response}) 

