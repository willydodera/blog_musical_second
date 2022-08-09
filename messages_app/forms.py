from django import forms
from .models import *

class UserSearchForm(forms.Form):
    username = forms.CharField(label='Usuario')


class MessageForm(forms.ModelForm):
    content = forms.CharField(label='Mensaje')

    class Meta:
        model = Message
        fields = ['content']



