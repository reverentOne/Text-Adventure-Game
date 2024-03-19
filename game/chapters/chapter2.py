from combat import combat_game as c

def chapter2(party):
    print("Welcome to Chapter 2: The Caves of Mystery!")
    print("You and your party have just entered the caves. You are surrounded by darkness and the sounds of dripping water. You have been tasked with finding the ancient relic hidden deep within the caves. You must fight your way through the caves and find the relic.")
    print("You have entered the first room of the caves. You are immediately attacked by a group of enemies!")
    floor = 6
    while True:
        print("Floor: ", floor)
        party = combat(party, floor)
        if len(party) == 0:
            print("Your party has been defeated. Game Over.")
            break
        if floor == 10:
            print("You have reached the end of the caves. You have found the ancient relic and have completed Chapter 2.")
            break
    return party