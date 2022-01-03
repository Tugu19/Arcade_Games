import random
from Ascii import DiceTitle
from Ascii import dices_ascii
import time
import os

def PlayerCount(dub, win, lose, p):
    if dub == "yes":
        lose -= 10
        win += 10
    else:
        lose -= 5
        win += 5
    if p == 1:
        print(f"Player1-> {win}  -  {lose} <-Player2")
    else:
        print(f"Player1-> {lose}  -  {win} <-Player2")
    time.sleep(5)
    os.system('cls')
    return win, lose

def DiceGame():
    os.system('cls')

    while True:
        print(DiceTitle)
        print("\n")
        print("Welcome to Dices Game!")
        print("1. Play")
        print("2. Back")
        inp = input(">")
        os.system('cls')

        money_p1 = 100
        money_p2 = 100

        if inp == '1':
            ok = 1
            player_turn = 1
            while True:
                if ok == 1:
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)
                    dice3 = random.randint(1, 6)
                    dice4 = random.randint(1, 6)

                #print(f"Dice1: {dice1}; Dice2: {dice2}")
                #print(f"Dice3: {dice3}; Dice4: {dice4}")

                if player_turn == 1:
                    print(dices_ascii[dice1-1])
                    print(dices_ascii[dice2-1])
                    print("""Player 1: Double points?
                            yes/no""")
                    double = input(">")

                    if double == 'quit':
                        break

                    if double != "yes" and double != "no":
                        print("Wrong command. Try again")
                        ok = 0
                        continue

                    print(dices_ascii[dice3 - 1])
                    print(dices_ascii[dice4 - 1])


                if player_turn == 2:
                    print(dices_ascii[dice3 - 1])
                    print(dices_ascii[dice4 - 1])
                    print("""Player 2: Double points?
                                                yes/no""")
                    double = input(">")

                    if double == 'quit':
                        break

                    if double != "yes" and double != "no":
                        print("Wrong command. Try again")
                        ok = 0
                        continue

                    print(dices_ascii[dice1 - 1])
                    print(dices_ascii[dice2 - 1])

                ok = 1
                if player_turn == 1:
                    player_turn = 2
                else:
                    player_turn = 1
                # 1---
                if dice1 == dice2 == 1 and dice3 == dice4 == 1:
                    print("Draw")
                    print(f"Player1-> {money_p1}  -  {money_p2} <-Player2")
                    time.sleep(5)
                    os.system('cls')
                    continue

                # 2---
                if dice1 == dice2 == 1 and dice3 == dice4 != 1 or dice1 == dice2 == 1 and dice3 != dice4:
                    print("Player 1 wins!")
                    money_p1, money_p2 = PlayerCount(double, money_p1, money_p2, 1)
                    continue

                elif dice3 == dice4 == 1 and dice1 == dice2 != 1 or dice3 == dice4 == 1 and dice1 != dice2:
                    print("Player 2 wins!")
                    money_p2, money_p1 = PlayerCount(double, money_p2, money_p1, 2)
                    continue

                # 3---
                if dice1 == dice2 and dice3 == dice4 and dice1 == dice3:
                    print("Draw")
                    print(f"Player1-> {money_p1}  -  {money_p2} <-Player2")
                    time.sleep(5)
                    os.system('cls')
                    continue

                # 4---
                if dice1 == dice2 and dice3 == dice4 and dice1 + dice2 > dice3 + dice4:
                    print("Player 1 wins!")
                    money_p1, money_p2 = PlayerCount(double, money_p1, money_p2, 1)
                    continue

                elif dice3 == dice4 and dice1 == dice2 and dice3 + dice4 > dice1 + dice2:
                    print("Player 2 wins!")
                    money_p2, money_p1 = PlayerCount(double, money_p2, money_p1, 2)
                    continue
                # 5---
                if dice1 == dice2 and dice3 != dice4:
                    print("Player 1 wins!")
                    money_p1, money_p2 = PlayerCount(double, money_p1, money_p2, 1)
                    continue

                elif dice3 == dice4 and dice1 != dice2:
                    print("Player 2 wins!")
                    money_p2, money_p1 = PlayerCount(double, money_p2, money_p1, 2)
                    continue
                # 6---
                if dice1 + dice2 > dice3 + dice4 and dice1 != dice2 and dice3 != dice4:
                    print("Player 1 wins!")
                    money_p1, money_p2 = PlayerCount(double, money_p1, money_p2, 1)
                    continue

                elif dice3 + dice4 > dice1 + dice2 and dice3 != dice4 and dice1 != dice2:
                    print("Player 2 wins!")
                    money_p2, money_p1 = PlayerCount(double, money_p2, money_p1, 2)
                    continue

                # 7---
                if dice1 + dice2 == dice3 + dice4:
                    print("Draw")
                    print(f"Player1-> {money_p1}  -  {money_p2} <-Player2")
                    time.sleep(5)
                    os.system('cls')
                    continue
        elif inp == '2':
            return 0

        else:
            print("\n   Unknown command. Try again.")
            time.sleep(3)
            os.system('cls')