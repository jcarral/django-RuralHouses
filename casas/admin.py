from django.contrib import admin
from .models import Casa

@admin.register(Casa)
class AdminCasa(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad')
    list_filter = ('ciudad', )
