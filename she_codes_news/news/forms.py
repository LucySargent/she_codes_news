from datetime import datetime
from django import forms
from django.forms import ModelForm
from .models import NewsStory #connecting the models in the news app

class StoryForm(ModelForm):
    class Meta: # nested class (or a meta class) - we want django to infer from
        model = NewsStory
        #list of fields to add to form - basically the fields from the NewStory model
        fields = ['title', 'pub_date', 'content']
        widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),}
        widgets = {'title': forms.TextInput(attrs={'style': 'border-color: purple;'}),}
        # widgets = {'content': forms.TextInput(attrs={'style': 'border-color: purple;'}),}
        # widgets = {'title': forms.TextInput(attrs={'style': 'margin-left: 30px;'}),}
