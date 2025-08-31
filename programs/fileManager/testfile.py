def fileStart():
    userQuestion = input("Would you like to read a file, edit a file, or create a new file? (r/e/c): ").lower()
    fileDirectory = "TextFiles"
    txtFileExtension = ".txt"
    fileName = input("Could you give me a file name?: ")
    file = fileDirectory + fileName + txtFileExtension 
    print(file)

fileStart()