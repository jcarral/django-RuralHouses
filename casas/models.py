from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Casa(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=2555)
    publico = models.BooleanField(default=False)
    imagen = models.ImageField(blank=True)
    postcode = models.CharField(max_length=15, blank=True)
    date = models.DateField(default=date.today, blank=True)
    numeroHabitaciones = models.IntegerField(default=0, blank=True)
    numeroBanios = models.IntegerField(default=0, blank=True)
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id', )

class Perfil(models.Model):
    #choices
    GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('I', 'Indefinido')
    )
    #Validadores
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #Extender el modelo de usuario
    user = models.OneToOneField(User, models.CASCADE, related_name='perfil')
    #Campos del Perfil
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)
    nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ('id', )
