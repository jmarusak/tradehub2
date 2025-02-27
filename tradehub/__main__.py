from tradehub.services import PartyService
from tradehub.datastore import Database

def main():
    db = Database("tradehub/datastore/database.json")
    partyService = PartyService(db)
    partyService.delete("0")
    parties = partyService.getAll()
    print(parties)

if __name__ == "__main__":
    main()
