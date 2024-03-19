from combat import combat_game as c
#Rest of imports needed

def chapter1(game_state):
    gs=game_state
    class enter():
        _location = "forest"

        def __init__(self):
            pl = gs["party_list"]
            gs["location"]["name"] = self._location
            gs["game_progress"]["chapter"] = 1
            #Rest of setting game state
            print("\nWelcome to Chapter 1: The Forest of Beginnings!")
            print("Your task is to find the ancient relic hidden deep within the forest. You are the guide master in charge of finding the right party to complete this task. Good luck!\n\n")
            party_str = '\n'.join([f"({i+1}) {str(party)}" for i, party in enumerate(pl)])
            party_num = int(input(f"Which party would you like to send?\n{party_str}\n"))-1
            print("Your team got a huge temperary booster!!!")
            boosted_party = pl[party_num].copy()
            for adventurer in boosted_party:
                adventurer.health += 10000
                adventurer.base_physical_damage += 1000
                adventurer.base_elemental_damage += 1000
            floor_reached = c.combat_loop(boosted_party)
            print("Your party reached floor: ", floor_reached)

            print("Now try again without the booster")
            floor_reached = c.combat_loop(pl[party_num].copy())
            print("Your party reached floor: ", floor_reached)
            print("Looks like you need to level up your party and give them items if you want to go further.")

    enter()
    return gs