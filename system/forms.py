from django import forms
from django.contrib.auth.models import User
from .models import userAccount

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), label = "Password")
    
    class Meta():
        model = User
        fields = ('username', 'password')
        labels = {'username': "User ID"}