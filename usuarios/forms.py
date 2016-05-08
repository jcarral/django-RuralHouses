from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
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
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-input'})
        self.fields['apellido'].widget.attrs.update({'class': 'form-input'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-input'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-input'})
        self.fields['genero'].widget.attrs.update({'class': 'form-input'})
        self.fields['avatar'].widget.attrs.update({'class': 'inputfile'})
