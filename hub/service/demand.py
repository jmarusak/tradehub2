from typing import Optional

from ..model import Demand
from ..mockdb import Database

class DemandService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, party: Demand) -> str:
        data = self.db.read()
        data["party"].append(party.model_dump())
        self.db.write()
        return party.party_id

    def get(self, party_id: str) -> Optional[Demand]:
        data = self.db.read()
        for row in data["party"]:
            if row["party_id"] == party_id:
               return Demand.model_validate(row)
        return None

    def getAll(self) -> list[Demand]:
        data = self.db.read()
        parties = data["party"]
        return [Demand.model_validate(party) for party in parties]

    def delete(self, party_id: str) -> None:
        data = self.db.read()
        for i, row in enumerate(data["party"]):
            if row["party_id"] == party_id:
                data["party"].pop(i)
        self.db.write()
