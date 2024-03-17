import drafting_party
from objects.item_generation import armor_generation, accessory_generation, weapon_generation, rarity, item_framework
from objects.enemy_generation import boss_enemy_generation, enemy_generator
import random
import time

defeated_enemies = []
defeated_bosses = []
party = drafting_party.draft_party()
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
                time.sleep(party_member.attack_speed)
                ability_speed_combat = party_member.ability_speed
                ability_speed_combat -= 1
                if party_member.base_physical_damage>0:
                    enemy_combat[0].health -= party_member.base_physical_damage/enemy_combat[0].physical_resistance
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
                    if party_member.elemental_base_physical_damage>0:
                        enemy_combat[0].health -= party_member.elemental_base_physical_damage/enemy_combat[0].elemental_resists
                        ability_speed_combat = party_member.ability_speed
                    weakest_member = min(active_party, key=lambda x: x.health)
                    weakest_member.health += weakest_member.healing
                    party_member.health += party_member.self_healing
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
                    if party_member.bleed_threshold_damage>0:
                        enemy_combat[0].bleed_threshold -= party_member.bleed_threshold_damage
                        if enemy_combat[0].bleed_threshold <= 0:
                            enemy_combat[0].health -= enemy_combat[0].health/10
                            enemy_combat[0].bleed_threshold = random.randint(200,1000)
                            if enemy_combat[0].health <= 0:
                                defeated_enemies.append(enemy[0])
                                for enemy in enemy_combat:
                                    if enemy in defeated_enemies:
                                        enemy_combat.remove(enemy)
                                    if enemy == None:
                                        break

            for enemy in enemy_combat:
                time.sleep(enemy.autoattack_speed)
                ability_speed_combat = enemy.ability_speed
                ability_speed_combat -= 1
                if enemy.base_physical_damage>0:
                    weakest_member.health -= enemy.base_physical_damage/active_party[weakest_member].physical_resistance
                if active_party[weakest_member].health <= 0:
                    active_party.remove(weakest_member)
                if ability_speed_combat == 0: 
                    if enemy.elemental_base_physical_damage>0:
                        weakest_member.health -= enemy.elemental_base_physical_damage/active_party[weakest_member].elemental_resists
                        ability_speed_combat = enemy.ability_speed
                    if enemy.self_healing>0:
                        enemy.health += enemy.self_healing
                    if active_party[weakest_member].health <= 0:
                        active_party.remove(weakest_member)
                    if enemy.bleed_threshold_damage>0:
                        weakest_member.bleed_threshold -= enemy.bleed_threshold_damage
                        if weakest_member.bleed_threshold <= 0:
                            weakest_member.health -= weakest_member.health/10
                            weakest_member.bleed_threshold = random.randint(100,400)
                            if active_party[weakest_member].health <= 0:
                                active_party.remove(weakest_member)

            for boss in boss_enemy_combat:
                time.sleep(boss.autoattack_speed)
                ability_speed_combat = boss.ability_speed
                ability_speed_combat -= 1
                if boss.base_physical_damage>0:
                    weakest_member.health -= boss.base_physical_damage/active_party[weakest_member].physical_resistance
                if active_party[weakest_member].health <= 0:
                    active_party.remove(weakest_member)
                if ability_speed_combat == 0: 
                    if boss.elemental_base_physical_damage>0:
                        weakest_member.health -= boss.elemental_base_physical_damage/active_party[weakest_member].elemental_resists
                        ability_speed_combat = boss.ability_speed
                    if boss.self_healing>0:
                        boss.health += boss.self_healing
                    if active_party[weakest_member].health <= 0:
                        active_party.remove(weakest_member)
                    if boss.bleed_threshold_damage>0:
                        weakest_member.bleed_threshold -= boss.bleed_threshold_damage
                        if weakest_member.bleed_threshold <= 0:
                            weakest_member.health -= weakest_member.health/10
                            weakest_member.bleed_threshold = random.randint(100,400)
                            if active_party[weakest_member].health <= 0:
                                active_party.remove(weakest_member)
            if len(enemy_combat) == 0:
                floor+=1
                break
    return(floor)


    #generate rewards based on defeated enemies and floor

