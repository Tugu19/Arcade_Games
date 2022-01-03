from AsciiScene import path1, path2, altPath1, altPath2, treasureTitle, crossedScene
import os
import time


def Treasure2():
    while True:
        os.system('cls')
        print(treasureTitle)
        print("Welcome to Treasure island game!")
        print("1. Play")
        print("2. Back")
        n = input("> ")
        os.system('cls')

        if n == '1':
            TreasureIsland()
        elif n == '2':
            return 0
        else:
            print("Wrong command")


def TreasureIsland():
    items = {
        "machete": 0, "cross": 0, "rune": 0, "curse": 0,
        "artefact": 0, "magic_stone": 0, "strange_key": 0,
        "odd_trinket": 0, "vampire_pendant": 0, "strange_box": 0,
        "scale": 0, "lucky_charm": 0, "horseshoe": 0,
        "amulet": 0, "fairy_crown": 0}

    sideItems = {
        "old_man_key": 0, "old_man_wand": 0, "vampire_key": 0
    }

    os.system('cls')
    print(crossedScene[0])
    print("""    The legend says that on a hidden island a huge treasure lise down on the
        bottom of a volcano. Some day a mighty adventurer will find the island and it's secrets!""")

    # time.sleep(7)
    print(crossedScene[3])
    print("""    You are on a ship trying to find that island. After a while you spotted 
        something that might be the legendary island.
        Before departing you have to choose one item to take in your expedition:
                            
        1.a machete
        2.a rune
        3.a small crossbow""")

    while True:
        m = input("> ")

        if m == '1':
            items["machete"] = 1
            break
        elif m == '2':
            items["rune"] = 1
            break
        elif m == '3':
            items["cross"] = 1
            break
        else:
            print("    Wrong command")

    os.system('cls')
    print(crossedScene[4])
    print("""    You stumbled a forked path. Which way will you go?
             
        1.Left
        2.Right """)

    while True:
        m = input("> ")
        if m == '1':
            os.system('cls')
            print(path1[0])
            print("    Far in the distance you see a small village")
            # time.sleep(5)
            os.system('cls')

            print(path1[1])
            print("""    At the entrance, a threat looking native appears in your way
                        
            1.salutes
            2.run """)
            if items["cross"] == 1:
                print("         3. use crossbow")

            k = 0
            while True:
                if k == 0:
                    m = input("> ")
                if m == '1':
                    if k == 0:
                        os.system('cls')
                        print(path1[2])
                        print("    He is happy to see that you're not a threat and welcomes you into the village")
                        time.sleep(5)

                    os.system('cls')
                    print(path1[4])
                    print("""    You entered a tavern. An old native offers you a drink
                    1.Take it
                    2.Refuse it""")

                    while True:
                        m = input("> ")
                        if m == '2':
                            os.system('cls')
                            print(path1[5])
                            print("    He is not upset that you refused him. You two started to talk and he tells you about a treasure inside a volcano")
                            time.sleep(5)

                            os.system('cls')
                            print(path1[6])
                            print("""    After hearing the story you packed up and before leaving the old man gave you the 
                            opportunity to take an item to you journey
                            
                            1.a key
                            2.a wand""")

                            while True:
                                m = input("> ")
                                if m == '1':
                                    sideItems["old_man_key"] = 1
                                    break
                                elif m == '2':
                                    sideItems["old_man_wand"] = 1
                                    break
                                else:
                                    print("    Wrong command")

                            os.system('cls')
                            print(path1[7])
                            print("""    You followed the path and found an old abandoned mansion
                                 1. Look for an entrance
                                 2. Continue the path""")
                            if sideItems["old_man_key"] == 1:
                                print("3. Use the key to open the door")

                            k = 0
                            while True:
                                if k == 0:
                                    m = input("> ")
                                if m == '1':
                                    os.system('cls')
                                    print(path1[8])
                                    print("No window was opened nor the door. You continued the path")
                                    time.sleep(5)
                                    k = 1
                                    m = '2'

                                elif m == '2':
                                    os.system('cls')
                                    print("    After a while...")

                                elif m == '3' and sideItems["old_man_key"] == 1:
                                    print(path1[8])
                                    print("    The key perfectly matched the lock. You entered the mansion")
                                    time.sleep(5)

                                    os.system('cls')
                                    print(altPath1[0])
                                    print("""    The mansion looks haunted. Where do you go first?
                                    1.Upstairs
                                    2.Living room
                                    3.Kitchen""")


                                    while True:
                                        if sideItems["vampire_key"] == 0:
                                            m = input("> ")

                                        if m == '1':
                                            os.system('cls')
                                            print(altPath1[3])
                                            print("""    You see two doors
                                            1.Right
                                            2.Left""")

                                            tr = 0
                                            while True:
                                                if tr == 0:
                                                    m = input("> ")

                                                if m == '1':
                                                    os.system('cls')
                                                    print(altPath1[4])
                                                    print("(You hear some footsteps)")
                                                    print("""The door is locked
                                                    1.Check footsteps
                                                    2.Go to the left door""")
                                                    if sideItems["vampire_key"] == 1:
                                                        print("3. Use key")

                                                    while True:
                                                        if tr == 1:
                                                            m = '2'
                                                            break

                                                        m = input("> ")
                                                        if m == '1' or m == '2':
                                                            os.system('cls')
                                                            print(crossedScene[2])
                                                            print("At the end of the corridor a vampire appeared. He thinks you're a thief and kills you")
                                                            return 0

                                                        elif sideItems["vampire_key"] == 1 and m == '3':
                                                            os.system('cls')
                                                            print(altPath1[5])
                                                            print("""The key worked! In the empty room you found a odd trinket
                                                            1.Take it
                                                            2.Leave it""")

                                                            while True:
                                                                m = input("> ")

                                                                if m == '1':
                                                                    items["odd_trinket"] = 1
                                                                    tr = 1
                                                                    break

                                                                elif m == '2':
                                                                    tr = 1
                                                                    break

                                                                else:
                                                                    print("Wrong command")
                                                        else:
                                                            print("Wrong command")


                                                elif m == '2':
                                                    os.system('cls')
                                                    print(altPath1[6])
                                                    print("(You feel someone is behind you)")
                                                    print("A strange star formation lights up the room. It's a planetarium. Is' stars are pointing to")
                                                    print("an entrance, the volcano entrance!")
                                                    time.sleep(6)

                                                    os.system('cls')
                                                    print(altPath1[7])
                                                    print("Right before leaving the room a vampire appears in front of you")
                                                    print("1. Push him away")

                                                    if items["cross"] == 1:
                                                        print("2. Use crossbow")
                                                        print("3. Try to explain why and how you entered the house")

                                                    if items["cross"] == 0:
                                                        print("2. Try to explain why and how you entered the house")

                                                    while True:
                                                        m = input(" >")
                                                        if m == '1':
                                                            os.system('cls')
                                                            print(crossedScene[2])
                                                            print("The vampire thinks you are a thief and kills you.")
                                                            return 0

                                                        elif m == '2':
                                                            os.system('cls')
                                                            print(altPath1[8])
                                                            print("He is amused about the story because he knows the old man")


                                                        elif m == '2' and items["cross"] == 1:
                                                            os.system('cls')
                                                            print(altPath1[9])

                                                        elif m == '3' and items["cross"] == 1:
                                                            print()

                                                else:
                                                    print("Wrong command")

                                        elif m == '2':
                                            os.system('cls')
                                            print(altPath1[2])
                                            print("    In the living room you can see a black shadow lying on a armchair. ")
                                            print("    You approached it and saw something a nightmare.")
                                            time.sleep(5)

                                            os.system('cls')
                                            print(crossedScene[2])
                                            print("    It was a vampire. He made a quick attack and killed you")
                                            return 0

                                        elif m == '3':
                                            print(altPath1[1])
                                            print("""    You find a hung key near some knives
                                            1.Take the key
                                            2.Take the knife""")

                                            liv = 0
                                            while True:
                                                if liv == 0:
                                                    m = input("> ")

                                                if m == '1':
                                                    os.system('cls')
                                                    print(altPath1[0])
                                                    print("""    You want to check what is the key good for
                                                    1.Go upstairs
                                                    2.Go in the living room""")

                                                    while True:

                                                        m = input("> ")
                                                        if m == '1':
                                                            sideItems["vampire_key"] = 1
                                                            m = '1'
                                                            break
                                                        elif m == '2':
                                                            liv = 1
                                                            break
                                                        else:
                                                            print("Wrong command")

                                                elif m == '2':
                                                    os.system('cls')
                                                    print(altPath1[0])
                                                    print('The knife is marked with a fine writing: "Made with pleasure for living room". ')
                                                    print("It may be a hint, so you decided to check the living room")

                                                    os.system('cls')
                                                    print(altPath1[2])
                                                    print("    In the living room you can see a black shadow lying on a armchair. ")
                                                    print("    You approached it and saw something a nightmare.")
                                                    time.sleep(5)

                                                    os.system('cls')
                                                    print(crossedScene[2])
                                                    print("    It was a vampire. He made a quick attack. You tried to defend yourself with"
                                                          "the knife but he killed you")
                                                    return 0


                                                else:
                                                    print("Wrong command")


                                        else:
                                            print("    Wrong command")

                                else:
                                    print("Wrong command")


                        elif m == '1':
                            os.system('cls')
                            print(crossedScene[2])
                            print("    The old man didn't know that poison can kill the travellers. You died")
                            return 0
                        else:
                            print("    Wrong command")

                elif m == '3' and items["cross"] == 1:
                    os.system('cls')
                    print(path1[3])
                    print("""    You killed him. No one sees what happened and you can enter the village.
            You are cursed.""")
                    items["curse"] = 1
                    items["cross"] = 0
                    time.sleep(5)
                    k = 1
                    m = '1'

                elif m == "2":
                    os.system('cls')
                    print(crossedScene[2])
                    print("He thought that you are suspicious and alarmed the others. They found and killed you")
                    time.sleep(7)
                    return 0

                else:
                    print("Wrong command")

        elif m == '2':
            pass
        else:
            print("Wrong command")
