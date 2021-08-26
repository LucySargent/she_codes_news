from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm

from django.views.generic import ListView
from news.models import NewsStory


# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfile(generic.DetailView):  
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'user'

class StoryListView(ListView):
    template_name = 'users/profile.html'
    model = NewsStory
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context








    

