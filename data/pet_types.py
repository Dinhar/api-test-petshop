from typing import TypedDict
from typing import Protocol


class PetData(TypedDict):
    id: int
    category: dict[str, int | str]
    name: str
    photoUrls: list[str]
    tags: list[dict[str, int | str]]
    status: str

class PetDataFactory(Protocol):
    def __call__(self, **fields: PetData) -> PetData: ...