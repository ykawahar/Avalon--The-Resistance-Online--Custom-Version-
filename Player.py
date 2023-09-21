class Player:
    def __init__(self, id, name, role) -> None:
        self.id = id
        self.name = name
        self.role = role
        self.roleName = self.role.name
        self.knownInfo = {}

    def updateKnownInfo(self, data):
        pass
    
    def startingInfo(self, playerData):
        gainedKnowledge = self.role.startingInfo(playerData)
        if gainedKnowledge is not None:
            self.knownInfo.update(gainedKnowledge)
    
    def printKnownInfo(self):
        print(f"--- {self.roleName} ---")
        if self.knownInfo:
            for playerData in self.knownInfo:
                if not playerData:
                    pass
                else:
                    dataName = self.knownInfo[playerData]["name"]
                    dataRole = self.knownInfo[playerData]["role"]
                    if dataRole == "Minion of Mordred" or dataRole == "Loyal Knight of Arthur":
                        print(f"{dataName} is a {dataRole}")
                    else :
                        print(f"{dataName} is {dataRole}")
        else:
            print("No known info")