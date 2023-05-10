from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from .filters import PersonaFilter
from .models import Persona, EstadoSalud
from .serializers import PersonaSerializer, EstadoSaludSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonaFilter
    ordering_fields = ['dni', 'nombre_completo']
    lookup_field = 'uuid'


class EstadoSaludViewSet(viewsets.ModelViewSet):
    queryset = EstadoSalud.objects.all()
    serializer_class = EstadoSaludSerializer


class EstadoSaludListCreateView(ListCreateAPIView):
    queryset = EstadoSalud.objects.all()
    serializer_class = EstadoSaludSerializer
