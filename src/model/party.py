from pydantic import BaseModel

class Party(BaseModel):
    party_id: str
    name: str
