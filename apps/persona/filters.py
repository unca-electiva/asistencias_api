from django_filters import rest_framework as filters

from .models import Persona


class PersonaFilter(filters.FilterSet):
    class Meta:
        model = Persona
        fields = ['dni', 'min_dni', 'nombre', 'sexo']

    min_dni = filters.NumberFilter(field_name='dni', lookup_expr='gte')
    nombre = filters.CharFilter(field_name='nombre_completo', lookup_expr='icontains')

