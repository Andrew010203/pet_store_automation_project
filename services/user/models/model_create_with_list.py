from pydantic import BaseModel

class WithListResponse(BaseModel):
    code: int
    type: str
    message: str