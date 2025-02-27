from pydantic import BaseModel
from typing import List

class Demand(BaseModel):
    """
    Demand data model
    """
    demand_id: str
    party_id: str
    title: str
    price: float
    description: str
    embedding: List[float]
