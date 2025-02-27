from typing import Optional

from ..models import Supply
from ..datastore import Database

class SupplyService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, supply: Supply) -> str:
        data = self.db.read()
        data["supply"].append(supply.model_dump())
        self.db.write()
        return supply.supply_id

    def get(self, supply_id: str) -> Optional[Supply]:
        data = self.db.read()
        for row in data["supply"]:
            if row["supply_id"] == supply_id:
               return Supply.model_validate(row)
        return None

    def getAll(self) -> list[Supply]:
        data = self.db.read()
        supplies = data["supply"]
        return [Supply.model_validate(supply) for supply in supplies]

    def delete(self, supply_id: str) -> None:
        data = self.db.read()
        for i, row in enumerate(data["supply"]):
            if row["supply_id"] == supply_id:
                data["supply"].pop(i)
        self.db.write()
