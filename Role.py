import abc
from abc import ABC, abstractclassmethod

### Possible parameters 
#       self.name = role name in String
#       self.desc =
#       self.affiliation = "Good" or "Evil"; which side
#       self.canFail = bool: if they can play Fail quest tokens
#       self.seenByMerlin = bool: if Merlin sees them as Evil at start
#       self.wakeAtStart = bool: Minions of Mordred that wake and see each other (Minions, Assassin, Mordred, Morgan)

class Role(ABC):
    def __init__(self) -> None:
        self.name = None
        self.desc = None

    def startingInfo(self, playerData):
        """Sort and store relevant information for the character.
            Called after roles are assigned in GameManager.

            Args:
                playerData(dict[]): Array of Dictionary of Player Data
            Returns:
                Fill knownAgents array.
        """

class Knight(Role):
    def __init__(self):
        super().__init__()
        self.affiliation = "Good"
        self.canFail = False
        self.name = "Loyal Knight of Arthur"
        self.seenByMerlin = False
        self.wakeAtStart = False
        

class Minion(Role):
    def __init__(self):
        super().__init__()
        self.affiliation = "Evil"
        self.canFail = True
        self.name = "Minion of Mordred"
        self.seenByMerlin = True
        self.wakeAtStart = True

    def startingInfo(self, playerData):
        """Wake at Start
            Minions of Mordred will see some other Minions of Mordred at the start of the game
        """
        foundInfo = {}
        for player in playerData:
            if player.role.wakeAtStart:
                info = {"id": player.id, "name": player.name, "role":"Minion of Mordred" }
                foundInfo[player.id] = info
        return foundInfo

class Merlin(Knight):
    def __init__(self):
        super().__init__()
        self.name = "Merlin"

    def startingInfo(self, playerData):
        """Clairvoyance
            Merlin can see Agents of Evil (Evil) players EXCEPT Mordred
            Agravain is GOOD but appears as Evil
        """
        foundInfo = {}
        for player in playerData:
            if player.role.seenByMerlin:
                info = {"id": player.id, "name": player.name, "role":"Evil" }
                foundInfo[player.id] = info
        return foundInfo

class Assassin(Minion):
    def __init__(self):
        super().__init__()
        self.name = "Assassin"
    











     