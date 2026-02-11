from typing import List, Optional
from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class PetResponse(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
