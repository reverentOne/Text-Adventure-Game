from idle_gameplay import IdleGameplay
import time
import numpy
from utils import save_load
#Rest of imports needed

def chapter1(game_state):
    gs=game_state
    idle_gameplay = IdleGameplay(gs)
    class enter():
        _location = "forest"

        def __init__(self):
            pl = gs["guild_member_matrix"]
            gs["location"]["name"] = self._location
            gs["game_progress"]["chapter"] = 1
            #Rest of setting game state
            print("\nWelcome to Chapter 1: The Forest of Beginnings!")
            print("Your task is to find the ancient relic hidden deep within the forest. You are the guide master in charge of finding the right party to complete this task. Good luck!\n\n")
            party_str = '\n'.join([f"({i+1}) {str(party)}" for i, party in enumerate(pl)])
            party_num = int(input(f"Which party would you like to send?\n{party_str}\n"))-1

            print("Your team got a huge temporary booster!!!")
            boosted_party = pl[party_num].copy()
            for adventurer in boosted_party:
                adventurer.health += 10000
                adventurer.base_physical_damage += 1000
                adventurer.base_elemental_damage += 1000

            idle_gameplay.start_adventure(boosted_party)

            print("Lets speed up the adventure by spending one diamond!")
            idle_gameplay.reduce_adventure_duration(0, 600000)
            print("...")
            #time.sleep(2)
            print("\nNow try again without the booster")
            adventure_thread = idle_gameplay.start_adventure(numpy.copy(pl[party_num]))
            print("Great! Now wait a few seconds for the adventure to finish.")

            # Wait for the adventure thread to finish before executing code under join()
            adventure_thread.join()
            print("\nWell that wasn't great...")
            #time.sleep(1)
            print("Looks like you need to level up your party and give them items if you want to go further.")

    enter()
    return gs