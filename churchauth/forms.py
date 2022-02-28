from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import LeadersModel


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LeadersForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = LeadersModel
 
        # specify fields to be used
        fields = "__all__"