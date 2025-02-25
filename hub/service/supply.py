from typing import Optional

from ..model import Supply
from ..mockdb import Database

class SupplyService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, party: Supply) -> str:
        data = self.db.read()
        data["party"].append(party.model_dump())
        self.db.write()
        return party.party_id

    def get(self, party_id: str) -> Optional[Supply]:
        data = self.db.read()
        for row in data["party"]:
            if row["party_id"] == party_id:
               return Supply.model_validate(row)
        return None

    def getAll(self) -> list[Supply]:
        data = self.db.read()
        parties = data["party"]
        return [Supply.model_validate(party) for party in parties]

    def delete(self, party_id: str) -> None:
        data = self.db.read()
        for i, row in enumerate(data["party"]):
            if row["party_id"] == party_id:
                data["party"].pop(i)
        self.db.write()
