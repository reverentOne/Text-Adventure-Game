from objects import adventurer_generation
#import enemy_generation
import random


def generator(odds):

    if odds < 45:
        return adventurer_generation.common_adventurer()
    elif odds < 60:
        return adventurer_generation.uncommon_adventurer()
    elif odds <80:
        return adventurer_generation.rare_adventurer()
    elif odds < 95:
        return adventurer_generation.epic_adventurer()
    else:
        return adventurer_generation.legendary_adventurer()

def draft_party():
    adventurers_list = []
    print("Welcome to your Adventurer Draft! Draft a party of 4 adventurers. You will get a choice from 3 random adventurers in each of 4 rounds. Choose wisely and good luck!\n")
    for _ in range(4):  
        print("Round " + str(_+1), "\n")
        adventurers_draft_list = []
        for _ in range(3):  
            print("Adventurer " + str(_+1), "\n")
            new_adventurer = generator(random.randint(0,100))
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
    return adventurers_list
draft_party()
