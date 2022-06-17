import pytest

from apps.core.tests.fixtures import api_client, get_default_test_user
from .fixtures import crear_programas


@pytest.mark.django_db
def test_api_lista_programas(api_client, crear_programas, get_default_test_user):
    client = api_client
    client.force_authenticate(user=get_default_test_user)
    response = client.get('/api/v1/programa/')
    assert response.status_code == 200
    json_data = response.json()

    assert len(json_data) == 2
    assert json_data[0]['nombre'] == 'COVID'
    assert json_data[1]['nombre'] == 'ASISTENCIA ALIMENTICIA'
