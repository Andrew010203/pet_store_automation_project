from pydantic import BaseModel

class PetResponseUpdateById(BaseModel):
    code: int
    type: str
    message: str