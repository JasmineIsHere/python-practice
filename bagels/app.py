from random import *
from tkinter.tix import MAX
# from PyDictionary import PyDictionary

# WORDLE CLONE
NUM_LETTERS = 6
MAX_GUESSES = 6

winning_text = ["BINGOOOOOOOOO", "GOALLLLLLLLL", "YAHOOO!!", "That's right!!!", "V^_^V", "YAYY", "WOOOOOO"]
guess = [" "] * NUM_LETTERS


def main():
    print(''' 
#######################################
########## HO HO HO WELCOME! ##########
#######################################
############# Bagels Game #############
############# By  Jasmine #############
#######################################
    ''')
    
    playGameStart = input("Do you want to play a game? (Y/N) ")
    playGame = True if playGameStart.lower() == "y" else False
    while playGame:
        selectGame = input("What game do you want to play? (Bagels/Wordle) ")
        if selectGame.lower() == "bagels":
            playBagel = True
            while playBagel:
                playBagel = bagel()
        elif selectGame.lower() == "wordle":
            wordle()
        else:
            print("HEY!")
        playGame = True if input("Do you still want play a game? (Y/N) ").lower() == "y" else False

    print ("BYE!")
        
def bagel():
    print('''
###########################################################
Welcome to BAGELS, a Math logic game. 

I am thinking of a 6 digits number. What number am I?

Clues:
Pico = one digit is correct but in the wrong position
Fermi = one digit is correct and in the right position
Bagel = no digit is correct
###########################################################
    ''')
    secretNum = getSecretNum()
    print("You have", MAX_GUESSES, "guesses")
    
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        #while they still have guesses left, continue
        guess = ""
        # keep looping until they get a valid guess
        invalidGuess = 0
        while len(guess) != NUM_LETTERS or not guess.isdecimal():
            invalidGuess += 1
            if (invalidGuess > 1):
                print("DUDE.")
                print("NUMBERS.")
                print("I NEED A 6. DIGIT. NUMBER.")
                print("Come on. Try Again.")
            print()
            print("Guess #{}: ".format(numGuesses))
            guess = input("> ")
        
        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1
        if guess == secretNum:
            break
        if numGuesses > MAX_GUESSES:
            print("...You ran out of guesses.")
            print("The answer was {}.".format(secretNum))
    return True if input("Do you want to play Bagel again? (Y/N) ").lower()=="y" else False

    

def getSecretNum():
    numbers = list('0123456789')
    shuffle(numbers)
    secret_num = ""
    for i in range(NUM_LETTERS):
        secret_num += str(randint(0,9))
    print("TEST|| secret_num:", secret_num)
    return secret_num

def getClues(guess, secretNum):
    if guess == secretNum:
        return choice(winning_text)
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)


def wordle():
    #TODO (write code)
    secretQns = getSecretWord()


def getSecretWord():
    #TODO (create a dictionary.txt of 6 letter words and return a random word)
    file = open("dictionary.txt", "r")

#run program
if __name__ == '__main__':
    main()