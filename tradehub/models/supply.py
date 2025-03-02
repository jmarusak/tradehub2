from pydantic import BaseModel
from typing import List

class Supply(BaseModel):
    """
    Supply data model
    """
    supply_id: str
    party_id: str
    title: str
    price: float
    description: str
    embedding: List[float]
