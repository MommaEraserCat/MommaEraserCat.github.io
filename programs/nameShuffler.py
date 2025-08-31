import random
import tkinter as tk

class nameShuffler:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Name Shuffler")

        self.mainWindow.geometry("800x600")
        self.mainWindow.minsize(400, 300)
        self.mainWindow.configure(bg="#bfcfff")

        self.canvas = tk.Canvas(self.mainWindow, height=300, width=500, background="#001861")

        self.TopFrame = tk.Frame(self.mainWindow, bg="#809fff")
        self.nameInputText = tk.Label(self.TopFrame, text="Input a name:")
        self.nameInput = tk.Entry(self.TopFrame, width=20)
        self.blankVariable = tk.StringVar()
        self.shuffledName = tk.Label(self.TopFrame, textvariable=self.blankVariable)

        self.BottomFrame = tk.Frame(self.mainWindow, bg="#809fff")
        self.nameButton = tk.Button(self.BottomFrame, width=13, text="Shuffle Name!", command=self.nameSorter)
        self.exitButton = tk.Button(self.BottomFrame, width=4, text="Exit", command=self.mainWindow.destroy)

        self.nameInputText.pack(padx=15, pady=2)
        self.nameInput.pack(padx=15, pady=2)
        self.shuffledName.pack(padx=15, pady=2)
        self.TopFrame.pack()

        self.nameButton.pack(padx=15, pady=2)
        self.exitButton.pack(padx=15, pady=2)
        self.BottomFrame.pack()
        nameShuffler.startedString()

        tk.mainloop()
    # Builds GUI

    def nameSorter(self):
        name = self.nameInput.get().lower()
        # shuffleString = f"Your name is {name} now." Try to see if you can have this variable be outside and accessed by the if statement
        # make sure to add a feature for people including last names
        if name == "joe":
            self.blankVariable.set("You are the chosen one.")
        elif name.startswith("j"):
            name = "Joe"
            self.blankVariable.set(name)
        elif not name.startswith("j"):
            name = "".join(random.sample(name, len(name))).capitalize()
            self.blankVariable.set(name)
    # Main code/Name changer

    def hasBeenCalled():
        nameShuffler.hasBeenCalled = True

    def startedString():
        print("Name Shuffler Started.\n")

def main():
    print("Starting Name Shuffler...\n")
    if nameShuffler.hasBeenCalled:
        nameShuffler()
    print("See ya!")

main()