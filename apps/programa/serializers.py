from rest_framework import serializers
from .models import TipoAsistencia, Programa, AsignacionBeneficio


class TipoAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAsistencia
        fields = '__all__'


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ('nombre', 'requisitos', 'fecha_inicio', 'fecha_fin', 'tipo_asistencias', )


class AsignacionBeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionBeneficio
        fields = '__all__'
