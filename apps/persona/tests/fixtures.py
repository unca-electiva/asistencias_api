import pytest

from apps.persona.models import Persona


@pytest.fixture
def crear_persona():
    persona,_ = Persona.objects.get_or_create(
        dni='27563896',
        nombre_completo='Laura Gonzalez',
        defaults={
            'fecha_nacimiento': '2000-12-13',
            'sexo': 'femenino',
            'domicilio': 'La Rioja 635'
        }
    )
    return persona
