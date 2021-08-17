from django import forms
from django.forms import ModelForm
from .models import NewsStory #connecting the models in the news app

class StoryForm(ModelForm):
    class Meta: # nested class (or a meta class) - we want django to infer from
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content'] #list of fields to add to form - basically the fields from the NewStory model
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date'}),
        }



