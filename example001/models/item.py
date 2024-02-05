from typing import Union, Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int
    name: str = Field(default="New Item")
    price: Optional[float] = None
    is_offer: Union[bool, None] = None