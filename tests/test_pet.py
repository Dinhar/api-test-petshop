import pytest
from api.api_client import ApiClient

class TestPet:

    @pytest.fixture(scope='session')
    def client(self) -> ApiClient:
        return ApiClient()

    def test_get_pet_data(self, client: ApiClient) -> None:
        response = client.get('/pet/findByStatus', params='status=available')
        print(response.text)