from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import CustomUser
from .forms import CustomUserCreationForm
from django.db import models

# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfile(DetailView):  
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'user'

    def get_queryset(models):
        my_stories = 










    

