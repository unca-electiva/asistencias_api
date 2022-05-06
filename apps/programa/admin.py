from django.contrib import admin

# Register your models here.
from .models import TipoAsistencia


@admin.register(TipoAsistencia)
class TipoAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('tipo',)
