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
            gs["game_progress"]["floor"] = 1
            fl = gs["game_progress"]["floor"]
            #Rest of setting game state
            print("\nWelcome to Chapter 1: The Forest of Beginnings!")
            print("Your task is to find the ancient relic hidden deep within the forest. You are the guide master in charge of finding the right party to complete this task. Good luck!\n\n")
            while True:
                party_num = int(input(f"Which party would you like to send? {pl}"))-1
                party = c.combat_loop(pl[party_num])    #, enemy_list(fl)) #need to define the enemy list function
                if fl == 5:
                    gs["game_progress"]["floor"] = fl
                    pl[party_num] = party
                    gs["party_list"] = pl
                    print("You have reached the end of the forest. You have found the ancient relic and have completed Chapter 1.")
                    break
                fl += 1
    enter()
    return gs