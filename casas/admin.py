from django.contrib import admin
from .models import Casa, Favorito, Oferta, Imagenes

@admin.register(Casa)
class AdminCasa(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad')
    list_filter = ('ciudad', )


@admin.register(Favorito)
class AdminFavorito(admin.ModelAdmin):
    list_display = ('id', 'casaFavorito', 'usuarioFavorito')
    list_filter = ('usuarioFavorito', 'casaFavorito' )

@admin.register(Oferta)
class AdminOferta(admin.ModelAdmin):
    list_display = ('id', 'casaOfertada', 'fechaInicio', 'fechaFin', 'precio')
    list_filter = ('casaOfertada', 'fechaInicio', 'fechaFin', 'precio')

admin.register(Imagenes)
