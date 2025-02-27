from pydantic import BaseModel, Field

class Party(BaseModel):
    """
    Party data model
    """
    party_id: str = Field(...)
    name: str = Field(...)
