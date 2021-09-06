from django.contrib.auth.forms import UsernameField
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic.detail import DetailView
# from django.shortcuts import render
from django.views.generic import ListView

from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin



# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfile(generic.DetailView):  
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'user'


class StoryListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'users/userStories.html'
    model = NewsStory
    
    # def get_queryset(self):
    #     context = super().get_queryset(self)
    #     context['user_stories'] = NewsStory.objects.all()
    #     return context

    def get_context_data(self, **kwargs):
        # print(self.request.GET.get('search'))
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author=self.request.user)
        return context








    

