import pytest


@pytest.mark.django_db
def test_api_lista_programas(crear_programas):

    client = APIClient()
response = client.get(reverse('pagina-list'))

assert response.status_code == 200
json_data = response.json()
meta = json_data['meta']
data = json_data['data']
