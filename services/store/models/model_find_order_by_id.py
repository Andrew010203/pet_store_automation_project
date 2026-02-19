from datetime import datetime
from pydantic import BaseModel, Field
from typing import Union


class FindOrderByIdResponse(BaseModel):
    id: int = Field(..., description="ID заказа")
    petId: int = Field(..., description="ID питомца")
    quantity: int = Field(..., description="Количество")
    shipDate: Union[datetime, str, None] = None
    status: str = Field(..., description="Статус заказа")
    complete: bool = Field(..., description="Завершен ли заказ")