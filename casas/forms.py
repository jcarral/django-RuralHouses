from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('nombre', 'apellido', 'telefono', 'genero', 'nacimiento', 'avatar', )
