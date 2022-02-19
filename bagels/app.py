import random
# from PyDictionary import PyDictionary

# WORDLE CLONE
NUM_LETTERS = 6
MAX_GUESSES = 6


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
    playGame = True if (playGameStart == "Y" or playGameStart == "y") else False
    while playGame:
        selectGame = input("What game do you want to play? (Bagel/Wordle) ")
        if selectGame == "Bagel":
            bagel()

        elif selectGame == "Wordle":
            wordle()
        else:
            print("HEY!")
    print ("BYE!")
        
def bagel():
    secretQns = getSecretNum()

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ""
    for i in range(NUM_LETTERS):
        secret_num += str(numbers[i])
    return secret_num

def wordle():
    #TODO (write code)
    secretQns = getSecretWord()

def getSecretWord():
    #TODO (create a dictionary.txt of 6 letter words and return a random word)
    file = open("dictionary.txt", "r")

main()