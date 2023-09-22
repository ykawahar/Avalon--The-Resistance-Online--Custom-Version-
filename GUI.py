import tkinter as tk

class TitleGUI:
    def __init__(self, root):
        self.titleWindow = root
        self.titleWindow.title("Avalon: The Resistance")

        self.titleWindow.config(bg="#955E42")

        # Dimensions of window
        # self.appWidth = 500
        # self.appHeight = 500
        # self.screenWidth = root.winfo_screenwidth()
        # self.screenHeight = root.winfo_screenheight()

        # self.titleWindow.geometry(f'{self.screenWidth}x{self.screenHeight}')

        self.createWidgets()

    
    def createWidgets(self):

        for i in range(5):
            tk.Grid.rowconfigure(root, i, weight=1)
            tk.Grid.columnconfigure(root, i, weight=1)
            

        # tk.Grid.rowconfigure(root, 0, weight=1)
        # tk.Grid.columnconfigure(root, 0, weight=1)
        titleLabel = tk.Label(self.titleWindow, anchor="center", text="Avalon:", 
                                        font = "Kokonor 40 bold", fg= "#E6CE63", bd=1, relief = "solid")
        titleLabel.grid(row = 0, column= 0, columnspan = 2, sticky="ew")
        subTitleLabel = tk.Label(self.titleWindow, text="The Resistance",
                                      font = "Kokonor 30 bold", fg= "#E6CE63", bd=1, relief = "solid")
        subTitleLabel.grid(row = 1, column= 0, columnspan = 2, sticky = "ew")

        #Player Number selection
        numPlayerLabel = tk.Label(self.titleWindow, text="Select Number of Players:", font = "Times 20")
        numPlayerLabel.grid(row = 3, column = 0)
        numPlayerSelection = tk.Spinbox(self.titleWindow, from_=5, to=10, width = 5)
        numPlayerSelection.grid(row = 3, column = 1, padx=10)


        #Buttons
        play = tk.Button(self.titleWindow, text="Play", font="Times 20 bold", bd=1, command = self.startGame)
        play.grid(row = 5, column = 0, columnspan=2)

        help = tk.Button(self.titleWindow, text="?", font = "Times 40", command = self.showHelp, width=3, relief = "raised", bg = "#D3D3D3")
        help.grid(row = 0, column = 4, sticky="ne")


    def startGame(self):
        print("Starting Game")

    def showHelp(self):
        print("Show Help")


if __name__ == "__main__":
    root = tk.Tk()
    TitleGUI(root)
    root.mainloop()


