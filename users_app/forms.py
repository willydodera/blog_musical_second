from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', "first_name"]
        help_texts = {k:"" for k in fields} #Saca los mensajes de ayuda


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', "first_name", "avatar"]
        help_texts = {k:"" for k in fields} #Saca los mensajes de ayuda


