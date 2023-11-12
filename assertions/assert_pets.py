from typing import Type, TypeVar
from httpx import Response
from pydantic import BaseModel

Pet = TypeVar('Pet', bound=BaseModel)

def assertion_model(response: Response, model: Type[Pet]):
    body = response.json()

    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)
