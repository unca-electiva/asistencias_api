from django.db.models import Count
from django_filters import rest_framework as filters

from .models import Programa


class ProgramaFilter(filters.FilterSet):
    class Meta:
        model = Programa
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'tipo_asistencias']

    con_asignacion_beneficio = filters.BooleanFilter(method='obtener_programas_con_beneficios',
                                                     label='Tiene Asignaciones de Beneficios?')

    def obtener_programas_con_beneficios(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(cantidad_asignaciones=Count(
                'asignaciones_beneficios',
                distinct=True)
            )
            return queryset.filter(cantidad_asignaciones__gt=0)

        return queryset
