from django.contrib.auth import get_user_model #django function
from django.db import models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # making the author set automatically to the logged in user
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE 
    ) #if user is deleted, their stories will be deleted too 
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.TextField(default = "")
    class Meta: 
        ordering = ['-pub_date']



