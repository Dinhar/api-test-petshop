import pytest
from api.api_client import ApiClient
from models.pet_models import PetModel
from data.pet_types import PetDataFactory
from assertions.assert_pets import assertion_model


class TestPet:

    @pytest.fixture(scope='session')
    def client(self) -> ApiClient:
        return ApiClient()

    def test_get_pet_data(self, client: ApiClient, pet_data_factory: PetDataFactory) -> None:
        response = client.get('/pet/13876545')
        pet_data = pet_data_factory()
        print(pet_data['id'])

        assertion_model(response, PetModel)
        

