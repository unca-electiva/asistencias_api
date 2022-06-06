from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from .filters import ProgramaFilter
from .models import Programa, AsignacionBeneficio, TipoAsistencia
from .serializers import ProgramaSerializer, AsignacionBeneficioSerializer


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgramaFilter
    ordering_fields = ['fecha_inicio', 'nombre']


class AsignacionBeneficioViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = AsignacionBeneficio.objects.all()
    serializer_class = AsignacionBeneficioSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['fecha_entrega', 'programa']

    def perform_create(self, serializer):
        # controlar que no se registren mas de 1 unidad de tipo-asistencia del tipo="comida"
        tipo_asistencia = serializer.validated_data.get('tipo_asistencia', None)
        cantidad = serializer.validated_data.get('cantidad', None)

        if tipo_asistencia.tipo == TipoAsistencia.COMIDA and cantidad > 1:
            raise ValidationError('La cantidad no puede ser mayor a 1 para asistencia de comida.')

        super().perform_create(serializer)
