
#import enemy_generation
import random
from utils.guild_manager import GuildManager
from objects.party import party
import numpy
from objects.adventurer_generation_2 import character
# draft a single character
def draft_character():
    print("Pick your adventurer! You will get a choice from 3 random adventurers. Choose wisely and good luck!\n")
    adventurers_draft_list = []
    for _ in range(3):  
        print("Adventurer " + str(_+1), "\n")
        new_adventurer = character()
        print(new_adventurer, "\n")
        adventurers_draft_list.append(new_adventurer)
    while True:
        choice = input("Choose Your Adventurer [type 1, 2 or 3] ")
        if choice in ['1', '2', '3']:
            choice = int(choice)
            break
        else:
            print("That is not an option.\n")
    if choice == 1:
        new_adventurer = adventurers_draft_list[0]
    elif choice == 2:
        new_adventurer = adventurers_draft_list[1]
    elif choice == 3:
        new_adventurer = adventurers_draft_list[2]
    print("You have chosen your adventurer.", "\n\n")
    print(adventurers_draft_list[0])
    return adventurers_draft_list[0]

#draft a party of 4 characters
def draft_party(game_state):
    adventurers_list = []
    print("Welcome to your Adventurer Draft! Draft a party of 4 adventurers. You will get a choice from 3 random adventurers in each of 4 rounds. Choose wisely and good luck!\n")
    for _ in range(4):  
        print("Round " + str(_+1), "\n")
        adventurers_draft_list = []
        for _ in range(3):  
            print("Adventurer " + str(_+1), "\n")
            new_adventurer = character()
            print(new_adventurer, "\n")
            adventurers_draft_list.append(new_adventurer)
        while True:
            choice = input("Choose Your Adventurer [type 1, 2 or 3] ")
            if choice in ['1', '2', '3']:
                choice = int(choice)
                break
            else:
                print("That is not an option.\n")


        if choice == 1:
            your_first_adventurer = adventurers_draft_list[0]
            adventurers_list.append(your_first_adventurer)

        elif choice == 2:
            your_first_adventurer = adventurers_draft_list[1]
            adventurers_list.append(your_first_adventurer)
        elif choice == 3:
            your_first_adventurer = adventurers_draft_list[2]
            adventurers_list.append(your_first_adventurer)

        print(your_first_adventurer)
        print("You have chosen your adventurer.", "\n\n")

    print("\nYour party is complete! Here are your adventurers:")
    for adventurer in adventurers_list:
        print("")
        print(adventurer)
    name = input("\nName your party:")
    party_array = numpy.array(adventurers_list) #convert list to array so it can be used in a matrix with your other parties
    new_party= GuildManager(game_state)
    new_party.guild_members(party_array, name)
    return party(name, adventurers_list, None, 1, 0), party_array