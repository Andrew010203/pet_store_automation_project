from pydantic import BaseModel
from datetime import datetime
from typing import Union, Optional

class OrderResponse(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: Union[datetime, str, None] = None
    status: str
    complete: bool