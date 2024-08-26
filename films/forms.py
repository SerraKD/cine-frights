from django import forms
from .models import NewsLetter

class NewsLetterForm(forms.ModelForm):
    ''' Newsletter field'''
    class Meta:
        model = NewsLetter
        fields = ('email',)