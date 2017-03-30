from django import forms
from .models import Tweet

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('name',)
