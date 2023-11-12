from pydantic import BaseModel

class PetModel(BaseModel):
    id: int
    category: dict[str, int | str]
    name: str
    photoUrls: list[str]
    tags: list[dict[str, int | str]]
    status: str
