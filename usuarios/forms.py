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
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'id': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'id': 'email'})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'id': 'txtNewPassword'})
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('nombre', 'apellido', 'telefono', 'genero', 'nacimiento', 'avatar', 'website', 'twitterAccount', 'facebookAccount')
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-input', 'id': 'firstname'})
        self.fields['apellido'].widget.attrs.update({'class': 'form-input'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-input'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-input'})
        self.fields['genero'].widget.attrs.update({'class': 'form-input'})
        self.fields['website'].widget.attrs.update({'class': 'u-full-width'})
        self.fields['twitterAccount'].widget.attrs.update({'class': 'u-full-width'})
        self.fields['facebookAccount'].widget.attrs.update({'class': 'u-full-width'})
        self.fields['avatar'].widget.attrs.update({'class': 'inputfile'})
