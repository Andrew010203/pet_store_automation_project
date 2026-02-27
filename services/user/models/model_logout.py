from pydantic import BaseModel

class LogoutResponse(BaseModel):
  code: int
  type: str
  message: str