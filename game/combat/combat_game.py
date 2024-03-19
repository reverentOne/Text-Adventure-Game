
import queue
from objects.enemy_generation import enemy_list
#import time
from drafting_party import draft_party
time = 0
def combat_loop(adventurers_list, flr = 0):
    global time
    if flr == 0: time = 0
    floor = flr
    enemy_party = enemy_list(floor)
    party = adventurers_list.members
    combat_queue = queue.PriorityQueue()
    weakest_adventurer = min(party, key=lambda x: x.health)
    weakenst_enemy = min(enemy_party, key=lambda x: x.health)
    while len(party) > 0:
        for adventurer in party:
            combat_queue.put((adventurer.attack_speed, adventurer))
        for enemy in enemy_party:
            combat_queue.put((enemy.attack_speed, enemy))
        ability_conter = 0
        while not combat_queue.empty():
            attack_speed, character = combat_queue.get()
            time += (1/attack_speed)
            if ability_conter <= 0:
                ability_conter = character.ability_speed
            ability_conter -= 1
            if character in adventurers_list:
                if len(enemy_party) != 0:
                    enemy_party[0].health -= max(1,character.base_physical_damage-enemy_party[0].physical_resistance)
                    if ability_conter <= 0:
                        enemy_party[0].health -= max(1,character.base_elemental_damage-enemy_party[0].elemental_resists)
                        weakest_adventurer.health += character.ally_healing
                        character.health += character.self_healing
                        bleed = enemy_party[0].bleed_threshold
                        bleed -= character.bleed_threshold_damage
                        if bleed <= 0:
                            enemy_party[0].health -= enemy_party[0].health/10
                            bleed = enemy_party[0].bleed_threshold
                    if enemy_party[0].health <= 0:
                        enemy_party.remove(enemy_party[0])
                        if len(enemy_party) == 0:
                            floor += 1
                            adventurers_list.members = party
                            return combat_loop(adventurers_list, floor)

            elif character in enemy_party:
                    if len(party) != 0:
                        if ability_conter <= 0:
                            ability_conter = character.ability_speed
                        ability_conter -= 1
                        weakest_adventurer.health -= max(1, character.base_physical_damage-weakest_adventurer.physical_resistance)
                        if ability_conter <= 0:
                            weakest_adventurer.health -= max(1, character.base_elemental_damage-weakest_adventurer.elemental_resists)
                            ability_conter = character.ability_speed
                            character.health += character.self_healing
                            weakenst_enemy.health += character.ally_healing
                            bleed = weakest_adventurer.bleed_threshold
                            bleed -= character.bleed_threshold_damage
                            if bleed <= 0:
                                weakest_adventurer.health -= weakest_adventurer.health/10
                                bleed = weakest_adventurer.bleed_threshold
                        if weakest_adventurer.health <= 0:
                            party.remove(min(party, key=lambda x: x.health))                                
                            if len(party) == 0:
                                print(f"You have been defeated in {time} seconds.")
                                break           
            else:
                break
    return floor