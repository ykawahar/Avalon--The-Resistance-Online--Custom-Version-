import random
from os import system, name
import Role
from Player import Player

TeamSetup = {5: (3, 2), 6: (4, 2), 7: (4, 3),
                 8: (5, 3), 9: (6, 3), 10: (6, 4)}
QuestsSetup = {5: (2, 3, 2, 3, 3), 6: (2, 3, 4, 3, 4), 7: (2, 3, 3, 4, 4),
              8: (3, 4, 4, 5, 5), 9: (3, 4, 4, 5, 5), 10: (3, 4, 4, 5, 5)}

class GameManager:
    def __init__(self, numPlayers = 5, roleList = ["Knight","Knight","Merlin","Minion","Assassin"], playerNames = None):
        self.numPlayers = numPlayers
        self.roleList = roleList
        self.playerNames = playerNames
        if playerNames == None: #default names if none given
            self.playerNames = self.initDefaultPlayerNames(self.numPlayers)
        self.roles = self.initRoles(roleList)

        self.playerData = self.assignRoles(self.playerNames, self.roles) # Randomly assign roles to players
        
        # self.showInfo(self.playerData)

        self.debugPrints()
        

    def initDefaultPlayerNames(self, numPlayers):
        """Creates a default list of player names.
            Names are "Player" and a number
        Args:
            numPlayers (int): Number of players in game
        Returns:
            str[]: List of player names in format of "Player n" 
        """
        playerNames = []
        for i in range(numPlayers):
            playerNames.append("Player " + str(i+1))
            # print("Added ", playerNames[i])
        return playerNames

    def initRoles(self, roleList):
        """Initializes roles in the game
        Args:
            roleList (str[]): List of role names to be added
        Returns:
            Role[]: Array of Role classes that correspond to the input role list 
        """
        localRoleList = []

        dictRoles = {"Knight": Role.Knight(), 
                     "Minion":Role.Minion(),
                     "Merlin":Role.Merlin(),
                     "Assassin":Role.Assassin(),
                     }
        for role in roleList:
            localRoleList.append(dictRoles[role])

        return localRoleList

    def assignRoles(self, players, roles):
        """Randomly assigns roles, and adds numeral IDs to players
            Roles are shuffled, then added in that shuffled order.
            IDs start from 1.
        Args:
            players (str[]): List of Player Names
            roles (Role[]): List of Roles
        Returns:
            array of Player class containing assigned roles
        """

        playerList = []
        shuffledRoles = random.sample(roles,len(roles))

        for x in range(self.numPlayers):
            playerData = Player(x+1, players[x], shuffledRoles[x]) # Create new Player class
            playerList.append(playerData)
        
        # print("PL", playerList)
        return playerList

    def rolesToString(self, roles):
        """Creates a string list of roles in the game.

        Args:
            roles (Role[]): List of roles in the game
        Returns:
            str[]: List of role names
        """
        roleCheck = []
        for role in roles:
            roleCheck.append(role.name)
        return roleCheck

    def printPlayerData(self, playerData):
        """Prints HasMap of Player Data.
        Args:
            playerData: Hashmap of player data (id(int), name(str), role(Role))
        Returns:
            Prints data
        """
        print("--- Player Data ---\n")
        for player in playerData:
        
            print("   " , player.name)
            print("\tID:" , player.id)
            print("\tRole:", player.roleName)

    def showInfo(self, playerData):
        for player in playerData:
            passkey = player.name
            print(passkey)
            while True:
                text = input("Revealing next info. Pass computer to " + passkey + ". Type " + passkey + " when ready.\n")
                if text != passkey:
                    continue
                else:
                    self.clear()
                    print("You are " + player.roleName)
                    break
            
            while True:
                text = input("Type CLEAR to clear info before passing to next player\n")
                if text!= "CLEAR":
                    continue
                else:
                    self.clear()
                    break

    def clear(self):
 
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def debugPrints(self):
        """ Printing created info """
        # print ("Players: ", self.playerNames)
        # print("Roles: ", self.rolesToString(self.roles))
        self.printPlayerData(self.playerData)

        """ Make and Print start info """
        for player in self.playerData:
            player.startingInfo(self.playerData)
            player.printKnownInfo()

        print("DONE")

if __name__ == "__main__":
    g = GameManager()


