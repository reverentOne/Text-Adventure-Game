import drafting_party
from enemy_generation import boss_enemy_generation, enemy_generator
import enemy_generation
import time
import item_generation
import adventurer_generation
defeated_enemies = []
party = drafting_party()
def combat():
    while len(party) > 0:
        enemy_combat = []
        if floor % 5 == 0:
            enemy_combat.append(boss_enemy_generation())
        else:
            for _ in range(3):
                enemy_combat.append(enemy_generator())
        while True:
            for party_member in party:
                time.sleep(party[party_member].auto_attack_speed)
                ability_speed_combat = party[party_member].ability_speed
                ability_speed_combat -= 1
                if party[party_member].damage>0:
                    enemy_combat[0].health -= party[party_member].damage/enemy[0].resist
                if enemy_combat[0].health <= 0:
                    defeated_enemies.append(enemy[0])
                    for enemy in enemy_combat:
                        if enemy in defeated_enemies:
                            enemy_combat.remove(enemy)
                        if enemy == None:
                            break
                if ability_speed_combat == 0:
                    if party[party_member].elemental_damage>0:
                        enemy_combat[0].health -= party[party_member].elemental_damage/enemy[0].elemental_resists
                        ability_speed_combat = party[party_member].ability_speed
                    weakest_member = min(party, key=lambda x: x.health)
                    weakest_member.health += weakest_member.healing
                    party[party_member].health += party[party_member].self_healing
                    if enemy_combat[0].health <= 0:
                        defeated_enemies.append(enemy[0])
                        for enemy in enemy_combat:
                            if enemy in defeated_enemies:
                                enemy_combat.remove(enemy)
                            if enemy == None:
                                break

            for enemy in enemy_combat:
                time.sleep(enemy_combat[enemy].autoattack_speed)
                ability_speed_combat = enemy_combat[enemy].ability_speed
                ability_speed_combat -= 1
                if enemy_combat[enemy].damage>0:
                    weakest_member.health -= enemy_combat[enemy].damage/party[weakest_member].resist
                if party[weakest_member].health <= 0:
                    party.remove(weakest_member)
                if ability_speed_combat == 0: 
                    if enemy_combat[enemy].elemental_damage>0:
                        weakest_member.health -= enemy_combat[enemy].elemental_damage/party[weakest_member].elemental_resists
                        ability_speed_combat = enemy_combat[enemy].ability_speed
                    if enemy_combat[enemy].self_healing>0:
                        enemy_combat[enemy].health += enemy_combat[enemy].self_healing
                    if party[weakest_member].health <= 0:
                        party.remove(weakest_member)
            if len(enemy_combat) == 0:
                floor+=1
                break
    #generate rewards based on defeated enemies and floor
                


