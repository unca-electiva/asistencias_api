import pytest


@pytest.fixture(scope='session')
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
