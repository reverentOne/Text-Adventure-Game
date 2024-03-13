import json
import random
global rarity
rarity = {'common':1, 'uncommon':1.25, 'rare':1.45, 'epic':1.65, 'legendary':2.0}
class item_framework:
    def __init__(self,item_name,chosen_rarity, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed):
        self.name = item_name
        self.rarity = chosen_rarity
        self.health = health
        self.damage = damage  
        self.elemental_damage = elemental_damage 
        self.bleed_threshold_damage = bleed_threshold_damage 
        self.resist = resist  
        self.elemental_resists = elemental_resists  
        self.bleed_threshold = bleed_threshold 
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.self_healing = self_healing
        self.healing = healing
        self.autoattack_speed = autoattack_speed
        self.ability_speed = ability_speed
    def __str__(self):
        return f"{self.name} is a {self.rarity} item with {self.health} health, {self.damage} damage, {self.elemental_damage} elemental damage, {self.bleed_threshold_damage} bleed threshold damage, {self.resist} resist, {self.elemental_resists} elemental resists, {self.bleed_threshold} bleed threshold, {self.critical_chance} critical chance, {self.critical_damage} critical damage, {self.self_healing} self healing, {self.healing} healing, {self.autoattack_speed} autoattack speed, and {self.ability_speed} ability speed."



def weapon_generation():
    global rarity
    weapon = item_framework
    chosen_rarity = random.choice(list(rarity.keys()))
    health = random.randint(0, 10)*rarity[chosen_rarity]
    damage = random.randint(0, 10)*rarity[chosen_rarity]
    elemental_damage = random.randint(0,10)*rarity[chosen_rarity]
    bleed_threshold_damage = random.randint(0,10)*rarity[chosen_rarity]
    resist = 0
    elemental_resists = 0
    bleed_threshold = 0
    critical_chance = random.uniform(0,.02)
    critical_damage = random.uniform(0,.02)
    self_healing = random.randint(0,10)
    healing = random.randint(0,10)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,10)
    weapon = item_framework("weapon", health,chosen_rarity, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return weapon
weapon_generation()
print(weapon_generation())
