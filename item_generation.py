import json
import random
global rarity
rarity = {'common':1, 'uncommon':1.25, 'rare':1.45, 'epic':1.65, 'legendary':2.0}
class item_framework:

    item_type = ['weapon', 'armor', 'accessory']
    
    def __init__(self,item_name,chosen_rarity, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed, item_type):
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
        self.item_type = item_type
    def __str__(self):
        return f"{self.name} is a {self.rarity} item with {self.health} health, {self.damage} damage, {self.elemental_damage} elemental damage, {self.bleed_threshold_damage} bleed threshold damage, {self.resist} resist, {self.elemental_resists} elemental resists, {self.bleed_threshold} bleed threshold, {self.critical_chance} critical chance, {self.critical_damage} critical damage, {self.self_healing} self healing, {self.healing} healing, {self.autoattack_speed} autoattack speed, and {self.ability_speed} ability speed."



def weapon_generation():
    global rarity
    item_type = 'weapon'
    weapon = item_framework
    chosen_rarity = random.choice(list(rarity.keys()))
    health = 0
    damage = random.randint(0, 10)*rarity[chosen_rarity]
    elemental_damage = random.randint(0,10)*rarity[chosen_rarity]
    bleed_threshold_damage = random.randint(0,10)*rarity[chosen_rarity]
    resist = 0
    elemental_resists = 0
    bleed_threshold = 0
    critical_chance = random.uniform(0,.02)
    critical_damage = random.uniform(0,.02)
    self_healing = 0
    healing = 0
    autoattack_speed = random.random()
    ability_speed = random.randint(0,10)
    weapon = item_framework("weapon", item_type,health,chosen_rarity, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return weapon
def armor_generation():
    global rarity
    item_type = 'armor'
    armor = item_framework
    chosen_rarity = random.choice(list(rarity.keys()))
    health = random.randint(0, 10)*rarity[chosen_rarity]
    damage = 0
    elemental_damage = 0
    bleed_threshold_damage = 0
    resist = random.randint(0,10)*rarity[chosen_rarity]
    elemental_resists = random.randint(0,10)*rarity[chosen_rarity]
    bleed_threshold = random.randint(0,10)*rarity[chosen_rarity]
    critical_chance = 0
    critical_damage = 0
    self_healing = random.randint(0,10)
    healing = random.randint(0,10)
    autoattack_speed = 0
    ability_speed = 0
    armor = item_framework("armor", item_type,health,chosen_rarity, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return armor
def accessory_generation():
    global rarity
    item_type = 'accessory'
    accessory = item_framework
    chosen_rarity = random.choice(list(rarity.keys()))
    health = random.randint(0, 10)*rarity[chosen_rarity]
    damage = random.randint(0, 10)*rarity[chosen_rarity]
    elemental_damage = random.randint(0,10)*rarity[chosen_rarity]
    bleed_threshold_damage = random.randint(0,10)*rarity[chosen_rarity]
    resist = random.randint(0,10)*rarity[chosen_rarity]
    elemental_resists = random.randint(0,10)*rarity[chosen_rarity]
    bleed_threshold =  random.randint(0,10)*rarity[chosen_rarity]  
    critical_chance = random.uniform(0,.02)
    critical_damage = random.uniform(0,.02)
    self_healing = random.randint(0,10)
    healing = random.randint(0,10)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,10)
    accessory = item_framework("accessory", item_type,health,chosen_rarity, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return accessory
weapon_generation()
print(weapon_generation())
