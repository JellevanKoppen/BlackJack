#BlackJack v 0.03

"""
To do:
- Graphics for the cards so it will become easier to play
- Player can split
- Player can double down
"""

import random
import itertools


SUITS = '♣♦♥♠'
RANKS = '46K32J8T9A5Q7'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
quitting = False
global dealerWins
global playerWins
global balance
balance = 25
dealerWins = 0
playerWins = 0
def Game():

    i = True
    while i == True:
        BlackJack = False
        global balance
        dealerCard = 0
        playerCard = 2
        correctBet = False
        print("...NEW GAME...")
        input("Press Enter to begin...")
        print("Your balance is:", balance)
        while True:
            x = True
            while x == True:                
                try:
                    bet = int(input("Place your bets: "))
                    x = False
                except:
                    print("Not a number")
            if bet > balance:
                print("You don't have enough for that bet")
            elif bet <= balance and bet > 0:
                break
            else: print("incorrect Value")
        balance = balance - bet
        

        handPlayer = random.sample(DECK, 2)
        handDealer = random.sample(DECK, 1)
        handDealer = list(itertools.chain(handDealer, ["  "]))

        worth = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

        def PlayerNumber(handPlayer):
            handPlayer1 = worth[handPlayer[0][0]]
            handPlayer2 = worth[handPlayer[1][0]]
            handPlayer = handPlayer1 + handPlayer2
            return(handPlayer)

        def DealerNumber(handDealer):
            handDealer = worth[handDealer[0][0]]
            return (handDealer)

        def Acer(array, points):
            for i in range(0, len(array)):
                if array[i][0] == "A":
                    if points > 21:
                        return i
                else: pass

        def Pay(bet):
            if BlackJack == True:
                return bet * 2.5
            else:
                return bet * 2.0

        def GameOver():
            global playerWins
            global dealerWins
            print("")
            print("Game Over")
            if winner == "PUSH":
                print("It's a tie, bets will be equally divided")
            else:
                print("The Winner is: ", winner)
            if winner == "PLAYER":
                playerWins += 1
            elif winner == "DEALER":
                dealerWins +=1
            print("Dealer: ", dealerWins, "wins")
            print("Player: ", playerWins, "wins")
            print("")
            i = False

        worthPlayer = PlayerNumber(handPlayer)
        worthDealer = DealerNumber(handDealer)

        print ("Dealer: ", handDealer, worthDealer)
        print ("Player: ", handPlayer, worthPlayer)


        if worthPlayer == 21 and len(handPlayer) == 2:
            winner = "PLAYER"
            print("PLAYER_BLACKJACK")
            GameOver()
            BlackJack = True
            price = Pay(bet)
            print("You won: ", price)
            balance += price
            break

        if handDealer[0][0] == "A":
            choice = input("Do you want to insure? (YES|NO): ")
            if choice.lower() == "yes":
                print("Okay insuring...")
            elif choice.lower() == "no":
                print("Whatever u want")        

        while worthPlayer <= 21:
            choice = input("hit or stand?: ")
            if choice.lower() == "hit":
                card = random.sample(DECK, 1)
                handPlayer = list(itertools.chain(handPlayer ,card))
                worthPlayer = worthPlayer + worth[handPlayer[playerCard][0]]
                playerCard += 1
                swap = Acer(handPlayer, worthPlayer)
                print(swap)
                if isinstance(swap, int):
                    suit = handPlayer[swap][1]
                    handPlayer[swap] = 'ace' + suit
                    worthPlayer = worthPlayer - 10
                print("Player: ", handPlayer, worthPlayer)

            if choice.lower() == "stand":
                break

        if worthPlayer > 21:
            print("PLAYER_BUST")
            winner = "DEALER"
            GameOver()
            break

        while worthDealer < 17:
            dealerCard += 1
            if dealerCard == 1:
                handDealer.remove("  ")
            card = random.sample(DECK, 1)
            handDealer = list(itertools.chain(handDealer ,card))
            worthDealer = worthDealer + worth[handDealer[dealerCard][0]]
            swap = Acer(handDealer, worthDealer)
            print(swap)
            if isinstance(swap, int):
                suit = handDealer[swap][1]
                handDealer[swap] = 'ace' + suit
                worthDealer = worthDealer - 10
            print("Dealer: ", handDealer, worthDealer)
        if worthDealer > 21:
            print("DEALER_BUST")
            winner = "PLAYER"
            price = Pay(bet)
            print("You won: ", price)
            balance += price
            GameOver()
            break

        elif worthDealer == 21 and len(handDealer) == 2:
            print("DEALER_BLACKJACK")
            winner = "DEALER"
            GameOver()
            break

        elif worthDealer > worthPlayer:
            winner = "DEALER"
            GameOver()
            break

        elif worthDealer < worthPlayer:
            winner = "PLAYER"
            price = Pay(bet)
            print("You won: ", price)
            balance += price
            GameOver()
            break

        elif worthDealer == worthPlayer:
            winner = "PUSH"
            balance += bet
            GameOver()
            break

        else:
            print("Unkwown error occured, quitting game now")
            GameOver()
            break

while quitting == False:
    Game()





