#Antoine Bonnet

# User Guess the Word: A hangman game

import random

print("-- Welcome to the hangman game! -- \n To install the game, please download the englishWords.txt file to your computer.")
foundFile = False
while(foundFile != True):
    path = input("Please write the absolute path of the englishWords.txt file in your computer.\nFor example: /Users/UserName/Desktop/englishWords.txt :\n")
    try:
        fp = open(path, "r",encoding="utf8", errors='ignore')
        foundFile = True
    except IOError:
            print("The path given is incorrect. Please try again")
            
# Create a dictionary of words with length larger than 6
minLength = 6
words = []
for word in fp.readlines():
    word = word.strip('\n')
    if (len(word) >= minLength):
        words.append(word)
fp.close()
def flatten(listLetters):
        word = ""
        for i in range(len(listLetters)):
            word += listLetters[i]
        return word
    
def guessWord(randWord):
    hiddenArray = []
    for i in range(len(randWord)):
        hiddenArray.append("_")

    hiddenWord = flatten(hiddenArray)
    print("Here is the word you must guess : ", hiddenWord)
    
    numGuesses= round(len(hiddenWord)*1.5)
    print("You start with", numGuesses, "guesses.")
    
    testedLetters = []
    wrongLetters = []
    
    while(numGuesses > 0):

        guessedWord = ""
        print("The word to guess is", flatten(hiddenArray))
        letter = input("Please input your letter guess : ")
        
        if (len(letter) != 1 or not letter.isalpha()):
            print("Incorrect input. Please try again")
            continue
        
        if (letter in testedLetters):
            print("You have already tried this letter. Try again.")
            continue
        
        testedLetters.append(letter)
        countSimilar = 0
        
        for i in range(len(randWord)):
            if (randWord[i] == letter):
                hiddenArray[i] = letter
                countSimilar += 1
            
        if (countSimilar == 0):
            wrongLetters.append(letter)
            numGuesses -= 1
            print("Wrong guess!") 
            print("Previous wrong guesses were:", wrongLetters)
            if numGuesses == 1:
                print("You have 1 guess left\n")
            elif numGuesses > 1 :
                print("You have", numGuesses, "guesses left\n")
            continue
        elif (hiddenArray.count("_") == 0):
            return 1
        else:
            print("Good guess!\n")
            
    return 0
    

#Start the game
while(True):
    print("Starting a new game!\n")
    # Pick a random word in the dictionary
    randomIndex = random.randint(0, len(words))
    randomWord = words[randomIndex]
    result = guessWord(randomWord)
    if result == 1:
        print("Congratulations! You have won. The word was", randomWord, "\n")
    else:
        print("You have no more guesses left. The word was", randomWord,"\n")
    
    

        






