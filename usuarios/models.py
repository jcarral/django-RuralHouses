from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Perfil(models.Model):
    #choices
    GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('I', 'Indefinido')
    )
    #Validadores
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #Relacionar el modelo de usuario
    user = models.OneToOneField(User, models.CASCADE, related_name='perfil')
    #Campos del Perfil
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)
    nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    twitterAccount = models.URLField(blank=True)
    facebookAccount = models.URLField(blank= True)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ('id', )
    def get_absolute_url(self):
        return "/user/%i/edit/" % self.id
