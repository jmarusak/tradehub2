from hub.model import Party
from hub.service import PartyService
from hub.mockdb import Database

def main():
    db = Database("hub/mockdb/database.json")
    partyService = PartyService(db)
    partyService.delete("0")
    parties = partyService.getAll()
    print(parties)

if __name__ == "__main__":
    main()
