import tkinter as tk
import tkinter.messagebox
import os


class TitleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Avalon")
        self.root.config(bg="#955E42")


if __name__ == "__main__":
    root = tk.Tk()
    TitleGUI(root)
    root.mainloop()
