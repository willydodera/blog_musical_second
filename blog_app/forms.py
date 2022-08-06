from django import forms
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Título')
    subtitle = forms.CharField(label='Subtitulo')
    content = forms.CharField(label='Contenido')

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'img']



