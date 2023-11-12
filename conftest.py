from dotenv import load_dotenv
import pytest
from mimesis.schema import Field, Schema
from mimesis.locales import Locale
from data.pet_types import PetData, PetDataFactory

def pytest_configure(config):
    load_dotenv(dotenv_path='.env')


@pytest.fixture()
def pet_data_factory() -> PetDataFactory:
    def factory(**fields) -> PetData:
        mf = Field(locale=Locale.RU)
        schema = Schema(schema=lambda: {
            'id': mf('random.randint', a=100, b=1000),
            'name': mf('person.first_name')
        })

        return {
            **schema.create()[0],
            **fields
        }
        
    return factory