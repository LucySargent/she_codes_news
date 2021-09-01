from datetime import datetime
from django import forms
from django.forms import ModelForm
from .models import NewsStory #connecting the models in the news app

class StoryForm(ModelForm):
    class Meta: # nested class (or a meta class) - we want django to infer from
        model = NewsStory
        #list of fields to add to form - basically the fields from the NewStory model
        fields = ['title', 'pub_date', 'content']
        widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date','style': 'margin-left: 12px;', 
        }),

        'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Story title here...', 
                'style': 'margin-left: 47px;',
        }),

        'content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Story content here...',
                'style': 'margin-left: 20px;',
                }),
        }

