from pydantic import BaseModel

class UpdatedUserResponse(BaseModel):
    code: int
    type: str
    message: str