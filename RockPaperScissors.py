import random
import os
from Ascii import RPSTitle

def RPSGame():
    while True:
        os.system('cls')
        print(RPSTitle)
        print("Welcome to Rock, Paper, Scissors!\n")
        print("1. Play")
        print("2. Back")
        n = int(input(">"))
        if n == 1:
            score_player = 0
            score_bot = 0
            while n == 1:
                print("Chose 1 for Rock, 2 for Paper, 3 for Scissors")
                print("Type 0 to exit")
                choose = int(input(">"))
                os.system('cls')
                bot = random.randint(1, 3)

                if choose == 1 and bot == 2:
                    print("""
            
                    You chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    Computer chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                     You lost 
                     (type 0 to exit)\n""")
                    score_bot += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")


                elif choose == 1 and bot == 3:
                    print("""
                    You chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    Computer chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    You won
                    (type 0 to exit)\n""")
                    score_player += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 1 and bot == 1:
                    print("""
                    You chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    Computer chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    It's a draw
                    (enter 0 to exit)\n""")
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 2 and bot == 1:
                    print("""
                    You chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                    Computer chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    You won
                    (enter 0 to exit)\n""")
                    score_player += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 2 and bot == 2:
                    print("""
                    You chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                    Computer chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                    It's a draw
                    (enter 0 to exit)\n""")
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 2 and bot == 3:
                    print("""
                    You chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                    Computer chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    You lost
                    (enter 0 to exit)\n""")
                    score_bot += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 3 and bot == 1:
                    print("""
                    You chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    Computer chose Rock
                    _______
                ---'    ____)
                          (_____)
                           (_____)
                           (____)
                ---.__(___)
            
                    You lost
                    (enter 0 to exit)\n""")
                    score_bot += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 3 and bot == 2:
                    print("""
                    You chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    Computer chose Paper
                    _______________
                ---'            ____)____
                                    ______)
                                   _______)
                                _______)
                ---.______________)
            
                    You won
                    (enter 0 to exit)\n""")
                    score_player += 1
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 3 and bot == 3:
                    print("""
                    You chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    You chose Scissors
                    ______________
                ---'         ______)___
                                  ______)
                              __________)
                         (______)
                ---.__(_____)
            
                    It's a draw
                    (enter 0 to exit)\n""")
                    print(f"Player -> {score_player} - {score_bot} <- Bot")

                elif choose == 0:
                    n = 0
                else:
                    print("Invalid number")
        elif n == 2:
            return 0
        else:
            print("Wrong command")