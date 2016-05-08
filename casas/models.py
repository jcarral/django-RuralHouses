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
    fecha = models.DateField(default=date.today, blank=True)
    numeroHabitaciones = models.IntegerField(default=0, blank=True)
    numeroBanios = models.IntegerField(default=0, blank=True)
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    mascotas = models.BooleanField(default=False)
    piscina = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id', )
