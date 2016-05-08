from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from .models import Perfil, Casa

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ('nombre', 'ciudad', 'direccion', 'publico', 'imagen', 'postcode', 'mascotas', 'piscina', 'numeroHabitaciones', 'numeroBanios', 'wifi', 'parking', 'descripcion',)
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
    def __init__(self, *args, **kwargs):
        super(CasaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-input'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-input'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-input'})
        self.fields['postcode'].widget.attrs.update({'class': 'form-input'})
        self.fields['numeroBanios'].widget.attrs.update({'class': 'form-input'})
        self.fields['numeroHabitaciones'].widget.attrs.update({'class': 'form-input'})
        self.fields['imagen'].widget.attrs.update({'class': 'inputfile'})



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
