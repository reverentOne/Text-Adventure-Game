import queue
from objects import adventurer_generation
from objects import enemy_generation
import random
import time
from drafting_party import draft_party
def combat(): #make party_list and enemy_list parameters
    enemy_party = [] # enemy_pary should be parameter, the creation of this party should be done elsewhere (posibly enemy_generation.py or in the chapters)
    party = draft_party() #this is unnecessary. Just call party_list instead of party
    combat_queue = queue.PriorityQueue()
    floor = 0
    weakest_adventurer = min(party, key=lambda x: x.health)
    weakenst_enemy = min(enemy_party, key=lambda x: x.health) # You can''t call enemy_party in Min() when it is empty
    while len(party) >= 0:
        if floor % 5 == 0 and floor != 0:
            enemy_party.append(enemy_generation.boss_enemy_generation())
        else:
            number_of_enemies = random.randint(1,4)
            for _ in range(number_of_enemies):
                enemy_party.append(enemy_generation.enemy_generator())
        for adventurer in party:
            combat_queue.put((adventurer.attack_speed, adventurer))
        for enemy in enemy_party:
            combat_queue.put((enemy.attack_speed, enemy))
        while not combat_queue.empty():
            attack_speed, character = combat_queue.get()
            time.sleep(1/attack_speed)
            ability_conter = character.ability_speed
            ability_conter -= 1
            if isinstance(character, adventurer_generation.adventurer_framework): #adventurer_framework is not a parameter so you can't call it like this
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
                    print(f"{enemy_party(0)} died")
                    if len(enemy_party) == 0:
                        floor += 1
                        break

            elif isinstance(character, enemy_generation.character_framework): #same as above
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
                        break
    if len(party) == 0:
        return floor
        
            
        




    
    
            
