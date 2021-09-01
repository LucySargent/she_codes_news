from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = {

        'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username',
        }),

        'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }),        
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']