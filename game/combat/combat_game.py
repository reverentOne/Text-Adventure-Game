
import queue
from enemy_generation import enemy_list
import random
import time
from drafting_party import draft_party
def combat_loop(adventurers_list, enemy_party):
    party = adventurers_list 
    combat_queue = queue.PriorityQueue()
    floor = 0
    weakest_adventurer = min(party, key=lambda x: x.health)
    weakenst_enemy = min(enemy_party, key=lambda x: x.health)
    for adventurer in party:
        combat_queue.put((adventurer.attack_speed, adventurer))
    for enemy in enemy_party:
        combat_queue.put((enemy.attack_speed, enemy))
    while not combat_queue.empty():
        attack_speed, character = combat_queue.get()
        time.sleep(1/attack_speed)
        ability_conter = character.ability_speed
        ability_conter -= 1
        if character in adventurers_list:
            if len(enemy_party) != 0:
                enemy_party[0].health -= character.damage/enemy_party[0].resist
                if ability_conter <= 0:
                    enemy_party[0].health -= character.elemental_damage/enemy_party[0].elemental_resists
                    ability_conter = character.ability_speed
                    weakest_adventurer.health += character.healing
                    character.health += character.self_healing
                    bleed = enemy_party[0].bleed_threshold
                    bleed -= character.bleed_threshold_damage
                    if bleed <= 0:
                        enemy_party[0].health -= enemy_party[0].health/10
                        bleed = enemy_party[0].bleed_threshold
                if enemy_party[0].health <= 0:
                    enemy_party.pop(0)
                    if len(enemy_party) == 0:
                        floor += 1
                        print("You have cleared the floor!")
                        break

        elif character in enemy_party:
            if len(party) != 0:
                weakest_adventurer.health -= character.damage/weakest_adventurer.resist
                if ability_conter <= 0:
                    weakest_adventurer.health -= character.elemental_damage/weakest_adventurer.elemental_resists
                    ability_conter = character.ability_speed
                    character.health += character.self_healing
                    weakenst_enemy.health += character.healing
                    bleed = weakest_adventurer.bleed_threshold
                    bleed -= character.bleed_threshold_damage
                    if bleed <= 0:
                        weakest_adventurer.health -= weakest_adventurer.health/10
                        bleed = weakest_adventurer.bleed_threshold
                if weakest_adventurer.health <= 0:
                    party.remove(weakest_adventurer)
                    if len(party) == 0:
                        print("You have been defeated.")
                        break
    if len(party) == 0:
        return floor


        
            
        




    
    
            
