from typing import Dict
from pydantic import RootModel

class InventoryResponse(RootModel):
    root: Dict[str, int]