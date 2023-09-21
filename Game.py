import GameManager

class Game:
    def __init__(self) -> None:
        self.main()
        self.numPlayers = None
        self.roles = []
        self.gameManager = None

    def main(self):
        self.startup()

    def startup(self):
        # numPlayers = int(input("How many players?\n"))
        self.gameManager = GameManager()
        pass



    


if __name__ == '__main__':
    g = Game()
              