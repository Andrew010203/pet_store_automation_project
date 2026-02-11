from pydantic import BaseModel

class ResponseImageModel(BaseModel):
  code: int
  type: str
  message: str