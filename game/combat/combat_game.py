
import queue
from objects.enemy_generation import enemy_list
#import time
from drafting_party import draft_party
time_counter = 0
def combat_loop(adventurers_list, flr = 0):
    global time_counter
    if flr == 0: time_counter = 0
    floor = flr
    enemy_party = enemy_list(floor)
    party = adventurers_list.members
    combat_queue = queue.PriorityQueue()
    weakest_adventurer = min(party, key=lambda x: x.health)
    weakenst_enemy = min(enemy_party, key=lambda x: x.health)
    ability_counters = {} # Initialize a dictionary to keep track of ability counters for each character

    #Main combat loop
    while len(party) > 0:
        #Add each adventurer and enemy to the combat queue
        for adventurer in party:
            combat_queue.put((adventurer.attack_speed, adventurer))
        for enemy in enemy_party:
            combat_queue.put((enemy.attack_speed, enemy))
        #process each character in the combat queue
        while not combat_queue.empty():
            #Get the character with the highest attack speed (lowest priority))
            attack_speed, character = combat_queue.get()
            #initialize ability counter for the character if it doesn't exist, then get it
            if character not in ability_counters:
                ability_counters[character] = character.ability_speed
            ability_counter = ability_counters[character]
            #Update the time counter
            time_counter += (1/attack_speed)

            if character in party:
                ability_counter -= 1
                if len(enemy_party) != 0:
                    #deal auto attack damage
                    enemy_party[0].health -= max(1,character.base_physical_damage-enemy_party[0].physical_resistance)
                    #deal ability damage if available
                    if ability_counter <= 0:
                        enemy_party[0].health -= max(1,character.base_elemental_damage-enemy_party[0].elemental_resists)
                        weakest_adventurer.health += character.ally_healing
                        character.health += character.self_healing
                        bleed = enemy_party[0].bleed_threshold
                        bleed -= character.bleed_threshold_damage
                        ability_counter = character.ability_speed
                        if bleed <= 0:
                            enemy_party[0].health -= enemy_party[0].health/10
                            bleed = enemy_party[0].bleed_threshold
                    #Update dictionary
                    ability_counters[character] = ability_counter
                    #resolve dead enemy
                    if enemy_party[0].health <= 0:
                        enemy_party.remove(enemy_party[0])
                        #if no more enemies, go to next floor
                        if len(enemy_party) == 0:
                            floor += 1
                            adventurers_list.members = party
                            return combat_loop(adventurers_list, floor)

            elif character in enemy_party:
                ability_counter -= 1
                if len(party) != 0:
                    weakest_adventurer.health -= max(1, character.base_physical_damage-weakest_adventurer.physical_resistance)
                    if ability_counter <= 0:
                        weakest_adventurer.health -= max(1, character.base_elemental_damage-weakest_adventurer.elemental_resists)
                        ability_counter = character.ability_speed
                        character.health += character.self_healing
                        weakenst_enemy.health += character.ally_healing
                        bleed = weakest_adventurer.bleed_threshold
                        bleed -= character.bleed_threshold_damage
                        if bleed <= 0:
                            weakest_adventurer.health -= weakest_adventurer.health/10
                            bleed = weakest_adventurer.bleed_threshold
                    ability_counters[character] = ability_counter
                    if weakest_adventurer.health <= 0:
                        party.remove(min(party, key=lambda x: x.health))                                 
                        if len(party) == 0:
                            print(f"You have been defeated in {time_counter} seconds.")
                            break           
            else:
                break
    return floor