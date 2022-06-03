import pytest
from apps.core.tests.fixtures import api_client, get_default_test_user
from apps.programa.models import AsignacionBeneficio
from apps.programa.tests.fixtures import crear_programas
from apps.persona.tests.fixtures import crear_persona


@pytest.mark.django_db
def test_api_creacion_asignacion_beneficio_correcto(api_client, get_default_test_user, crear_programas, crear_persona):
    client = api_client
    client.force_authenticate(user=get_default_test_user)

    programa1, programa2 = crear_programas
    persona = crear_persona
    tipo_asistencia = programa1.tipo_asistencias.first()

    data = {
        "fecha_entrega": "2022-06-03T13:08:00Z",
        "cantidad": "1",
        "programa": programa1.id,
        "persona": persona.id,
        "tipo_asistencia": tipo_asistencia.id
    }

    response = client.post('/api/v1/asignacion-beneficio/', logging=get_default_test_user, data=data)
    assert response.status_code == 201

    assert AsignacionBeneficio.objects.filter(
        persona=persona, programa=programa1, tipo_asistencia=tipo_asistencia, fecha_entrega='2022-06-03T13:08:00Z'
    ).count() == 1
