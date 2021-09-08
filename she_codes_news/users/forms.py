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
                'style': 'width: 100%',
        }),

        'email': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Email',
                'style': 'width: 100%',
                }),        
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']