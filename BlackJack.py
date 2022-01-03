import random
import os
import Cards
import time
from Ascii import blackTitle


def Selector(k):
    num = random.randint(1, 4)
    if num == 1:
        return Cards.BlackH[k]
    elif num == 2:
        return Cards.Heart[k]
    elif num == 3:
        return Cards.Clubs[k]
    else:
        return Cards.Diamonds[k]


def Calculator(k):
    if k > 10:
        return 10
    else:
        return k

def Black_Jack():

    os.system('cls')

    print(blackTitle)
    print("Welcome to the BlackJack\n")


    while True:
        print("Choose the game Style")
        print("1. Player VS Pc")
        print("2. Player VS Player")
        print("3. Back")
        n = int(input("> "))

        if n == 3:
            os.system('cls')
            return 0


        if n > 3:
            print("Wrong command")
            continue

        os.system('cls')
        # print((Cards.BlackH[2] + Cards.BlackH[5]))

        print("Select the number of players (between 1 and 4)")
        numb = int(input("> "))

        os.system('cls')


        player_number = 0

        playersTotal = [0, 0, 0, 0, 0]
        dealerCard = random.randint(0, 12)

        while player_number < numb:

            okAce = 0
            sumPlayer = 0
            playerCards = []

            card1 = random.randint(0, 12)
            card2 = random.randint(0, 12)

            playerCards.append(Selector(card1))
            playerCards.append(Selector(card2))

            sumPlayer += Calculator(card1+1) + Calculator(card2+1)
            print(f"{playerCards[0]} {playerCards[1]}")

            if card1 == 0 or card2 == 0:
                print(f"The total is: {sumPlayer} or {sumPlayer + 10}")
                okAce = 1
            else:
                print(f"The total is: {sumPlayer}")



            while True:
                if sumPlayer > 21:
                    print("You lost!")
                    time.sleep(3)
                    os.system('cls')
                    playersTotal[player_number] = 0
                    break
                if sumPlayer == 21:
                    time.sleep(7)
                    continue

                print(f"Dealer card: {Selector(dealerCard)}")
                print("1. Hit     2. Stand")
                nextCard = int(input(">  "))

                if nextCard == 2:
                    if okAce == 1:
                        playersTotal[player_number] = sumPlayer + 10
                    else:
                        playersTotal[player_number] = sumPlayer
                    os.system('cls')
                    break

                elif nextCard == 1:
                    os.system('cls')
                    card1 = random.randint(0, 12)
                    playerCards.append(Selector(card1))
                    sumPlayer += Calculator(card1+1)
                    for i in playerCards:
                        print(i)

                    if okAce == 1 or card1 == 0 and sumPlayer + 10 <= 21:
                        print(f"The total is: {sumPlayer} or {sumPlayer + 10}")
                    elif sumPlayer + 10 > 21:
                        print(f"The total is: {sumPlayer}")


                else:
                    print("Wrong command, try again.")
                    time.sleep(3)

            player_number += 1

        if n == 1:
            print("Dealer Turn: ")
            playerCards = [Selector(dealerCard)]
            sumPlayer = 0
            card1 = dealerCard
            card2 = random.randint(0, 12)
            playerCards.append(Selector(card2))
            sumPlayer += Calculator(card1 + 1) + Calculator(card2 + 1)



            while True:
                os.system('cls')
                for i in playerCards:
                    print(i)
                if sumPlayer > 21:
                    playersTotal[-1] = 0
                    break


                if sumPlayer >= 17 and sumPlayer <= 21 and sumPlayer >= playersTotal[0] and sumPlayer >= playersTotal[1] and sumPlayer >= playersTotal[2] and sumPlayer >= playersTotal[3]:
                    playersTotal[-1] = sumPlayer
                    break

                else:
                    card1 = random.randint(0, 12)
                    playerCards.append(Selector(card1))
                    sumPlayer += Calculator(card1 + 1)



            print(f"The total dealer cards is: {sumPlayer}")



            if max(playersTotal[0], playersTotal[1], playersTotal[2], playersTotal[3]) <= playersTotal[-1] and playersTotal[-1] <= 21:
                print("Dealer wins!")
                time.sleep(7)
                os.system('cls')
                continue

        max_val = max(playersTotal)
        winners = []
        i = 0
        while i < len(playersTotal):
            if playersTotal[i] == max_val:
                winners.append(str(i+1))
            i += 1
        print(f"The winning player/players are: {', '.join(winners)}")
        time.sleep(6)
        os.system('cls')