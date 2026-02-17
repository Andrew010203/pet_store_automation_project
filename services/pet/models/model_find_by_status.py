from typing import Optional
from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int
    name: Optional[str] = None

class Tag(BaseModel):
    id: int
    name: Optional[str] = None

class PetResponseFindByStatus(BaseModel):
    id: int
    category: Optional[Category] = None
    name: Optional[str] = None
    photoUrls: list[Optional[str]] = None
    tags: list[Optional[Tag]] = None
    status: str
