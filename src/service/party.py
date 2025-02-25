from ../model import Party

class PartyService:
    def __init__(self):
        self.parties = []

    def create(self, name):
        party = Party(name)
        self.parties.append(party)
        return party

    def get(self, name):
        for party in self.parties:
            if party.name == name:
                return party
        return None

    def list(self):
        return self.parties

    def delete(self, name):
        party = self.get(name)
        if party:
            self.parties.remove(party)
            return party
        return
