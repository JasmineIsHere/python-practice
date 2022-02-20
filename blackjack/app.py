from random import *
from sys import *

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backside"

def main():
    print('''
#######################################
######### A game of BlackJack #########
#######################################

Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play you can (D)ouble down to increase 
    your bet but must hit exactly one more time before standing.
    In case of a tie, the bet is is returned to the player.
    The dealer stops hitting at 17.
    ''')
    money = 5000
    
    playGame = True if input("Do you want to play a game? (Y/N) ").lower() == "y" else False
    while playGame:
        if money <= 0:
            print("BOOO!!! You are broke!")
            print("Good thing you weren't playing with real money!")
            print("Gamble responsibly. Call 1800-6-668-668 for help.")
            print("Thank you for playing!")
            exit()
        
        print("You have $" + str(money))
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Bet:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}".format(bet))
                print("Bet: ", bet)
            
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank,suit))
                playerHand.append(newCard)
                
                if getHandValue(playerHand) > 21:
                    #player busted
                    continue

            elif move in ("S"):
                break
        
        ## dealer's turn to draw
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    #dealer busted
                    break
                input("Press Enter to continue > ")
            
            #show final hands
            displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #check who won
        if dealerValue > 21:
            print("DEALER busts! You win ${}".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You Lost!")
            money -= bet
        elif playerValue > dealerValue:
            print("You won ${}".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you")
        
        input("Press Enter to continue > ")
        print("\n\n")


def getBet(maxBet):
    while True:
        print()
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Good choice. See you again.")
            exit()
        
        if not bet.isdecimal():
            print("HEY.")
            print("I need a NUMBER.")
            continue

        bet = int(bet)
        if bet < 0:
            print("HEY.")
            print("I need a POSITIVE NUMBER.")
        elif bet > maxBet:
            print("HEY.")
            print("YOU DON'T EVEN HAVE THAT MUCH MONEY @#$%&!")
            print("You have $" + str(maxBet))
        else:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) # numbered cards
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit)) 
    
    shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    ## hide the player's cards and dealer's cards.
    ## hide the dealer's first card if showDealerHand is False
    print()
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        # hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    
    ## show player's card
    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    ## return total value of hand
    value = 0
    numAces = 0
    for card in cards:
        rank = card[0] #card(rank, suit)
        if rank == 'A':
            numAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    # add values of aces
    value += numAces
    for i in range(numAces):
        if value + 10 <= 21:
            value += 10
    
    return value


def displayCards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += "___ "
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tand"]
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move 
        elif move == 'D' and "(D)ouble down" in moves:
            return move



if __name__ == "__main__":
    main()