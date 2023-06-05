from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from .filters import ProgramaFilter
from .models import Programa, AsignacionBeneficio, TipoAsistencia
from .serializers import ProgramaSerializer, AsignacionBeneficioSerializer


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgramaFilter
    ordering_fields = ['fecha_inicio', 'nombre']


class AsignacionBeneficioViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = AsignacionBeneficio.objects.all()
    serializer_class = AsignacionBeneficioSerializer


# se crea esta clase para ejemplificar el uso de vistas concretas
class AsignacionBeneficioListCreateView(ListCreateAPIView):
    queryset = AsignacionBeneficio.objects.all()
    serializer_class = AsignacionBeneficioSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['-fecha_entrega']

    # se sobrescribe el metodo para listar solo los beneficios del programa indicado en la URL
    def list(self, request, *args, **kwargs):
        programa = get_object_or_404(Programa, pk=kwargs['pk'])

        queryset = self.filter_queryset(self.get_queryset())

        # se filtran registros
        queryset = queryset.filter(programa=programa)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Tambien se puede sobrescribir este metodo en lugar de list() para filtrar por programa
    # def get_queryset(self):
    #     programa = get_object_or_404(Programa, pk=self.kwargs['pk'])
    #     queryset = super().get_queryset()
    #     return queryset.filter(programa=programa)

    def perform_create(self, serializer):
        programa = get_object_or_404(Programa, pk=self.kwargs['pk'])

        # controlar que no se registren mas de 1 unidad de tipo-asistencia del tipo="comida"
        tipo_asistencia = serializer.validated_data.get('tipo_asistencia', None)
        cantidad = serializer.validated_data.get('cantidad', None)

        if tipo_asistencia.tipo == TipoAsistencia.COMIDA and cantidad > 1:
            raise ValidationError('La cantidad no puede ser mayor a 1 para asistencia de comida.')

        serializer.save(programa=programa)
