from __future__ import unicode_literals

from django.db import models

class Casa(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    publico = models.BooleanField()
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id', )
