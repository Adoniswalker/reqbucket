from django import forms
from django.forms import ModelForm

from . import models


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='100 char max')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class RequestForm(ModelForm):
    class Meta:
        model = models.EndPoint
        fields = ['url_name']
