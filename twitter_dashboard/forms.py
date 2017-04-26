from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('user_name', 'date_tweeted', 'tweet', 'location')
