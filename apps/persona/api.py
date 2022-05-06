from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import PersonaFilter
from .models import Persona, EstadoSalud
from .serializers import PersonaSerializer, EstadoSaludSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonaFilter
    ordering_fields = ['dni', 'nombre_completo']


class EstadoSaludViewSet(viewsets.ModelViewSet):
    queryset = EstadoSalud.objects.all()
    serializer_class = EstadoSaludSerializer
