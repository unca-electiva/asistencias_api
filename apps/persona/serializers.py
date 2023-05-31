from rest_framework import serializers
from .models import Persona, EstadoSalud


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['uuid', 'dni', 'nombre_completo', 'fecha_nacimiento',
                  'sexo', 'domicilio']


class EstadoSaludSerializer(serializers.ModelSerializer):
    #persona = serializers.StringRelatedField()
    nombre_persona = serializers.SerializerMethodField(method_name='obtener_persona')

    class Meta:
        model = EstadoSalud
        fields = ['persona', 'nombre_persona', 'es_discapacitado', 'posee_obesidad', 'posee_desnutricion', 'observaciones']
        read_only_fields = ['nombre_persona']

    def obtener_persona(self, obj):
        return obj.persona.nombre_completo
