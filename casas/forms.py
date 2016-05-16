from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from .models import Casa


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
        self.fields['ciudad'].widget.attrs.update({'class': 'form-input city-input'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-input'})
        self.fields['postcode'].widget.attrs.update({'class': 'form-input'})
        self.fields['numeroBanios'].widget.attrs.update({'class': 'form-input'})
        self.fields['numeroHabitaciones'].widget.attrs.update({'class': 'form-input'})
        self.fields['descripcion'].widget.attrs.update({'class': 'u-full-width form-input'})
        self.fields['imagen'].widget.attrs.update({'class': 'inputfile'})
