from rest_framework import serializers
from .models import Persona, EstadoSalud


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['dni', 'nombre_completo', 'fecha_nacimiento',
                  'sexo', 'domicilio']


class EstadoSaludSerializer(serializers.ModelSerializer):
    #persona = serializers.StringRelatedField()

    class Meta:
        model = EstadoSalud
        fields = '__all__'
