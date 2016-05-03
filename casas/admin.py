from django.contrib import admin
from .models import Casa, Perfil

@admin.register(Casa)
class AdminCasa(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad')
    list_filter = ('ciudad', )

@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_filter = ('nombre', )
