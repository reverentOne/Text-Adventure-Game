from combat import combat

def chapter1(party):
    print("Welcome to Chapter 1: The Forest of Beginnings!")
    print("You and your party have just entered the forest. You are surrounded by tall trees and the sounds of nature. You have been tasked with finding the ancient relic hidden deep within the forest. You must fight your way through the forest and find the relic.")
    print("You have entered the first room of the forest. You are immediately attacked by a group of enemies!")
    floor = 1
    while True:
        print("Floor: ", floor)
        party = combat(party, floor)
        if len(party) == 0:
            print("Your party has been defeated. Game Over.")
            break
        if floor == 5:
            print("You have reached the end of the forest. You have found the ancient relic and have completed Chapter 1.")
            break
    return party