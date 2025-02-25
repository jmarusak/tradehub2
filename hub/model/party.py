from pydantic import BaseModel, Field

class Party(BaseModel):
    party_id: str = Field(...)
    name: str = Field(...)
