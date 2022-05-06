import pytest

from apps.core.tests.fixtures import api_client, get_default_test_user
from .fixtures import crear_programas


@pytest.mark.django_db
def test_api_lista_programas(api_client, crear_programas, get_default_test_user):
    client = api_client
    client.force_authenticate(user=get_default_test_user)
    response = client.get('/api/v1/programa/', logging=get_default_test_user)
    assert response.status_code == 200
    json_data = response.json()

