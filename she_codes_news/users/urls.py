from django.urls import path
from .views import CreateAccountView, UserProfile, StoryListView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    path('<int:pk>/', UserProfile.as_view(),name='userProfile'),
    path('userstories/', StoryListView.as_view(), name='myStories'),
]