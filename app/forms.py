from .models import Url
from django import forms

class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ['url']

        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }