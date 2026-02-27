from pydantic import BaseModel

class LogsUserIntoTheSystemResponse(BaseModel):
  code: int
  type: str
  message: str