from typing import Optional

from ..models import Demand
from ..datastore import Database

class DemandService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, demand: Demand) -> str:
        data = self.db.read()
        data["demand"].append(demand.model_dump())
        self.db.write()
        return demand.demand_id

    def get(self, demand_id: str) -> Optional[Demand]:
        data = self.db.read()
        for row in data["demand"]:
            if row["demand_id"] == demand_id:
               return Demand.model_validate(row)
        return None

    def getAll(self) -> list[Demand]:
        data = self.db.read()
        demands = data["demand"]
        return [Demand.model_validate(demand) for demand in demands]

    def delete(self, demand_id: str) -> None:
        data = self.db.read()
        for i, row in enumerate(data["demand"]):
            if row["demand_id"] == demand_id:
                data["demand"].pop(i)
        self.db.write()
