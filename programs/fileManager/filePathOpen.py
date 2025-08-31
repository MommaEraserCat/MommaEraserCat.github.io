import subprocess
import os

fileMode = "|Blank|"
interChangString = "Please type in the file name of the file you'd like to {} from: ".format(fileMode)

class textFileManager:
    def fileStart(self):
        userQuestion = input("Would you like to read a file, edit a file, or create a new file? (r/e/c): ").lower()
        self.fileDirectory = r"C:\Users\austi\Desktop\TextFiles\\"
        self.txtFileExtension = ".txt"
        
        if userQuestion == "r":
            textFileManager.fileReader(self)
        elif userQuestion == "e":
            textFileManager.fileEdit(self)
        elif userQuestion == "c":
            textFileManager.fileCreater(self)

    def fileReader(self):
        fileMode = "read"
        interChangString = "Please type in the file name of the file you'd like to {} from: ".format(fileMode)
        readTF = input(interChangString)
        file = self.fileDirectory + readTF + self.txtFileExtension
        fileOpened = open(file)
        print(fileOpened.read())

    def fileEdit(self):
        userQuestionTwo = input("Would you like to append or write to the file? (a/w): ").lower()
        if userQuestionTwo == "a":
            fileMode = "append"
            interChangString = "Please type in the file name of the file you'd like to {} to: ".format(fileMode)
            appendTF = input(interChangString)
            file = self.fileDirectory + appendTF + self.txtFileExtension
            appendMessage = input("What would you like to add to the end of this file?: ")
            with open(file, "a") as fileOpened:
                fileOpened.write(appendMessage) 
            with open(file) as fileOpened:
                print(fileOpened.read())
        elif userQuestionTwo == "w":
            fileMode = "write"
            interChangString = "Please type in the file name of the file you'd like to {} in: ".format(fileMode)
            writeTF = input(interChangString)
            file = self.fileDirectory + writeTF + self.txtFileExtension
            writeMessage = input("What would you like to change the text to in this file?: ")
            with open(file, "w") as fileOpened:
                fileOpened.write(writeMessage) 
            with open(file) as fileOpened:
                print(fileOpened.read())

    def fileCreater(self):
        createTF = input("Please name the new text file you'd like to create: ")
        file = self.fileDirectory + createTF + self.txtFileExtension
        fileCreated = open(file, "x")
        addiTextQues = input("Would you like to add anything to this file? (y/n): ").lower()
        if addiTextQues == "y":
            addiTextTF = input("What would you like to add to this file?: ")
            with open(file, "w") as fileOpened:
                fileOpened.write(addiTextTF)
            with open(file) as fileOpened:
                print(fileOpened.read())
        elif addiTextQues == "n":
            print("Alright, the file has been created then!\nBye!")
        else:
            print("Error")

def main():
    print("Starting File Manager...\n")
    textFileManager().fileStart()
    ''' Alright, so what you are trying to do rn, is make the damn thing work. When you hit run, nothing happens. See if it has to do with init
    otherwise see how init works with a normal class not using tkinter. Ugh.. I'm very upset at this tbh. | It works now since I learned that I
    gotta call the method :)'''

main()