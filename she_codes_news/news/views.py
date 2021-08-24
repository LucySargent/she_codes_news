from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):  
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        print(self.request.GET.get('search'))
        search_var = self.request.GET.get('search',"")
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:3]
        # context['all_stories'] = NewsStory.objects.order_by('-pub_date')[3:100]
        # context['latest_stories'] = NewsStory.objects.order_by('-pub_date').filter(title__contains=search_var)[:3]
        # context['all_stories'] = NewsStory.objects.order_by('-pub_date').filter(title__contains=search_var)[3:]
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').filter(author__username__contains=search_var)[:3]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').filter(author__username__contains=search_var)[3:]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm #from \news\forms.py
    context_object_name = 'storyForm' #just a name for the object
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index') #the path we can post things to when they are succesful

    #overiding form_valid on generic.CreateView
    def form_valid(self, form):
        #set author to logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
