from party_draft import draft_party
from item_generation import armor_generation, accessory_generation, weapon_generation, rarity, item_framework
from enemy_generation import boss_enemy_generation, enemy_generator

import time

defeated_enemies = []
defeated_bosses = []
party = draft_party()
def combat():
    floor = 0
    active_party = []
    for party_member in party:
        active_party.append(party_member)
    while len(active_party) > 0:
        enemy_combat = []
        boss_enemy_combat = []
        if floor % 5 == 0:
            enemy_combat.append(boss_enemy_generation())
        else:
            for _ in range(3):
                boss_enemy_combat.append(enemy_generator())
        while True:
            for party_member in active_party:
                time.sleep(active_party[party_member].auto_attack_speed)
                ability_speed_combat = active_party[party_member].ability_speed
                ability_speed_combat -= 1
                if active_party[party_member].damage>0:
                    enemy_combat[0].health -= active_party[party_member].damage/enemy[0].resist
                if boss_enemy_combat[0].health <= 0:
                    defeated_bosses.append(boss[0])
                    for boss in boss_enemy_combat:
                        if boss in defeated_bosses:
                            boss_enemy_combat.remove(boss)
                        if boss == None:
                            break
                if enemy_combat[0].health <= 0:
                    defeated_enemies.append(enemy[0])
                    for enemy in enemy_combat:
                        if enemy in defeated_enemies:
                            enemy_combat.remove(enemy)
                        if enemy == None:
                            break
                if ability_speed_combat == 0:
                    if active_party[party_member].elemental_damage>0:
                        enemy_combat[0].health -= active_party[party_member].elemental_damage/enemy[0].elemental_resists
                        ability_speed_combat = active_party[party_member].ability_speed
                    weakest_member = min(active_party, key=lambda x: x.health)
                    weakest_member.health += weakest_member.healing
                    active_party[party_member].health += active_party[party_member].self_healing
                    if boss_enemy_combat[0].health <= 0:
                        defeated_bosses.append(boss[0])
                        for boss in boss_enemy_combat:
                            if boss in defeated_bosses:
                                boss_enemy_combat.remove(boss)
                            if boss == None:
                                break
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
                    weakest_member.health -= enemy_combat[enemy].damage/active_party[weakest_member].resist
                if active_party[weakest_member].health <= 0:
                    active_party.remove(weakest_member)
                if ability_speed_combat == 0: 
                    if enemy_combat[enemy].elemental_damage>0:
                        weakest_member.health -= enemy_combat[enemy].elemental_damage/active_party[weakest_member].elemental_resists
                        ability_speed_combat = enemy_combat[enemy].ability_speed
                    if enemy_combat[enemy].self_healing>0:
                        enemy_combat[enemy].health += enemy_combat[enemy].self_healing
                    if active_party[weakest_member].health <= 0:
                        active_party.remove(weakest_member)

            for boss in boss_enemy_combat:
                time.sleep(boss_enemy_combat[boss].autoattack_speed)
                ability_speed_combat = boss_enemy_combat[boss].ability_speed
                ability_speed_combat -= 1
                if boss_enemy_combat[boss].damage>0:
                    weakest_member.health -= boss_enemy_combat[boss].damage/active_party[weakest_member].resist
                if active_party[weakest_member].health <= 0:
                    active_party.remove(weakest_member)
                if ability_speed_combat == 0: 
                    if boss_enemy_combat[boss].elemental_damage>0:
                        weakest_member.health -= boss_enemy_combat[boss].elemental_damage/active_party[weakest_member].elemental_resists
                        ability_speed_combat = boss_enemy_combat[boss].ability_speed
                    if boss_enemy_combat[boss].self_healing>0:
                        boss_enemy_combat[boss].health += boss_enemy_combat[boss].self_healing
                    if active_party[weakest_member].health <= 0:
                        active_party.remove(weakest_member)
            if len(enemy_combat) == 0:
                floor+=1
                break
    return(floor)
    rarity_chance = floor*len(enemy_combat)*10*len(boss_enemy_combat)

    #generate rewards based on defeated enemies and floor

draft_party()
combat()

