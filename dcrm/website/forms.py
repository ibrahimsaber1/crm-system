from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signupform(UserCreationForm):
    email = forms.EmailField(label="", widget= forms.TextInput('class': 'form-control', 'placeholder': "Enter Ypur Email : "))
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)