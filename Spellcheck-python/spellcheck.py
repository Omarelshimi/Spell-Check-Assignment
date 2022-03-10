# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

from operator import truediv
import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    loop = True
    while loop:
        print(f'''
        Main Menu 
        1: Spell Check a Word (Linear Search)
        2: Spell Check a Word (Binary Search)
        3: Spell Check Alice In Wonderland (Linear Search)
        4: Spell Check Alice In Wonderland (Binary Search)
        5: Exit
        ''')
        selection = input("Type a number corresponding with it's option please: ")
        if selection == "1":
                    word = input("Please enter a word: ")
                    startTime = time.perf_counter()
                    print(linearSearch(dictionary, word))
                    endTime = time.perf_counter()
                    print(str(endTime - startTime) + " seconds")
# end main()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def dictionarySearch():
    file = open("dictionary.txt")
    search_word = input()
    if(search_word == file):
        print("word found")
    else:
        print("Word not found.")
# Call main() to begin program
main()
