
import queue
from objects.enemy_generation import enemy_list
import time
from drafting_party import draft_party
def combat_loop(adventurers_list, flr = 0):
    floor = flr
    enemy_party = enemy_list(floor)
    party = adventurers_list 
    combat_queue = queue.PriorityQueue()
    weakest_adventurer = min(party, key=lambda x: x.health)
    weakenst_enemy = min(enemy_party, key=lambda x: x.health)
    while len(party) > 0:
        for adventurer in party:
            combat_queue.put((adventurer.attack_speed, adventurer))
        for enemy in enemy_party:
            combat_queue.put((enemy.attack_speed, enemy))
        while not combat_queue.empty():
            attack_speed, character = combat_queue.get()
            time.sleep(1/attack_speed)
            if ability_conter <= 0:
                ability_conter = character.ability_speed
            ability_conter -= 1
            if character in adventurers_list:
                if len(enemy_party) != 0:
                    enemy_party[0].health -= character.damage/enemy_party[0].resist
                    if ability_conter <= 0:
                        enemy_party[0].health -= character.elemental_damage/enemy_party[0].elemental_resists
                        weakest_adventurer.health += character.healing
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
                            combat_loop(party, floor)
                            print("You have cleared the floor!")
                            return floor
                    else:
                        return floor

                elif character in enemy_party:
                    if len(party) != 0:
                        if ability_conter <= 0:
                            ability_conter = character.ability_speed
                        ability_conter -= 1
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
                                return floor
                    else:
                        return floor
    if len(party) == 0:
        return floor


        
            
        




    
    
            
