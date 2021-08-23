from django.urls import path
from . import views #the . stands for the directory/module the current file is located
#'she_codes_news\news\views.py' and she_codes_news\news\urls.py are on same directory level 
#views.py has 'IndexView', 'StoryView' and 'AddStoryView'

app_name = 'news' # /news/ 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /news/ (Home page)
    #views.IndexView is the file+view 
    #name = 'index' is a name for the url
    path('<int:pk>/', views.StoryView.as_view(), name='story'), # /news/+primary key id for an individual story
    path('add-story/', views.AddStoryView.as_view(),name='newStory') # /news/add-story (our new story) 
]
