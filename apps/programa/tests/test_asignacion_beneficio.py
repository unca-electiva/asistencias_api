import pytest
from apps.core.tests.fixtures import api_client, get_default_test_user
from apps.programa.models import AsignacionBeneficio, TipoAsistencia
from apps.programa.tests.fixtures import crear_programas
from apps.persona.tests.fixtures import crear_persona


@pytest.mark.parametrize(
    'tipo_asistencia, cantidad, codigo_http, total_registros, loguear_usuario',
    [(TipoAsistencia.DINERO, 2, 401, 0, False),
     (TipoAsistencia.DINERO, 3, 201, 1, True),
     (TipoAsistencia.COMIDA, 2, 400, 0, True)]
)
@pytest.mark.django_db
def test_api_creacion_asignacion_beneficio(api_client, get_default_test_user, crear_programas, crear_persona,
                                                    tipo_asistencia, cantidad, codigo_http, total_registros, loguear_usuario):
    client = api_client
    if loguear_usuario:
        client.force_authenticate(user=get_default_test_user)

    programa1, programa2 = crear_programas
    persona = crear_persona
    tipo_asistencia = programa1.tipo_asistencias.filter(tipo=tipo_asistencia).first()

    data = {
        "fecha_entrega": "2022-06-03T13:08:00Z",
        "cantidad": cantidad,
        "programa": programa1.id,
        "persona": persona.id,
        "tipo_asistencia": tipo_asistencia.id
    }

    response = client.post(f'/api/v1/programa/{programa1.id}/asignacion-beneficio/', data=data)
    assert response.status_code == codigo_http

    assert AsignacionBeneficio.objects.filter(
        persona=persona, programa=programa1, tipo_asistencia=tipo_asistencia, fecha_entrega='2022-06-03T13:08:00Z'
    ).count() == total_registros


# Como este test tenia la misma funcionalidad, fue incluido en el anterior, mediante el envio de parametros
@pytest.mark.django_db
def test_api_creacion_asignacion_beneficio_cantidad_incorrecta(api_client, get_default_test_user, crear_programas, crear_persona):
    client = api_client
    client.force_authenticate(user=get_default_test_user)

    programa1, programa2 = crear_programas
    persona = crear_persona
    tipo_asistencia = programa1.tipo_asistencias.filter(tipo=TipoAsistencia.COMIDA).first()

    data = {
        "fecha_entrega": "2022-06-03T13:08:00Z",
        "cantidad": "2",
        "programa": programa1.id,
        "persona": persona.id,
        "tipo_asistencia": tipo_asistencia.id
    }

    response = client.post(f'/api/v1/programa/{programa1.id}/asignacion-beneficio/', logging=get_default_test_user, data=data)
    assert response.status_code == 400

    assert AsignacionBeneficio.objects.filter(
        persona=persona, programa=programa1, tipo_asistencia=tipo_asistencia, fecha_entrega='2022-06-03T13:08:00Z'
    ).count() == 0
