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
            dictionaryLs()
        elif selection == "2":
            dictionaryBs()
        elif selection == "3":
            words = 0
            for index in dictionary:
                if index == aliceWords:
                    words += 1
                    print("Number of words found: " + words)
        elif selection == "5":
            print("Program Closed")
            loop = False                       
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

def binarySearch(anArray, item):
    lowerIndex = 0
    higherIndex = len(anArray) - 1
   
    while lowerIndex <= higherIndex:
        middleIndex = (higherIndex + lowerIndex) // 2
        if anArray[middleIndex] == item:
            return middleIndex
        elif item < anArray[middleIndex]:
            higherIndex = middleIndex - 1
        else:
            lowerIndex = middleIndex + 1
    return -1

def dictionaryLs(dictionary, word):
    word = input("Please enter a word: ")
    startTime = time.perf_counter()
    index = linearSearch(dictionary, word)
    if index == -1:
        endTime = time.perf_counter()
        print("Not Found")
    else:
        endTime = time.perf_counter()
        print("Position " + str(index) + " Took " + str(endTime - startTime) + " seconds") 
def dictionaryBs(dictionary, word):
    word = input("Please enter a word: ")
    startTime = time.perf_counter()
    index = binarySearch(dictionary, word)
    if index == -1:
        endTime = time.perf_counter()
        print("Not Found")
    else:
        endTime = time.perf_counter()
        print("Position " + str(index) + " Took " + str(endTime - startTime) + " seconds")

# Call main() to begin program
main()
