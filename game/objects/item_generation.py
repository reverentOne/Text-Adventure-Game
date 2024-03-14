import json
import os
config_path = os.path.join('assets', 'data', 'config.json')
import random
from enum import Enum
class rarity(Enum): 
    common = 1
    uncommon = 1.25
    rare = 1.45
    epic = 1.65
    legendary = 2.0

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    ACCESSORY = "accessory"

    
class item_framework:

    ItemType = ['weapon', 'armor', 'accessory']
    
    def __init__(self,item_name,chosen_rarity, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed, item_type):
        item_type = ItemType(item_type)
        if item_type not in ItemType:
            raise ValueError(f"Invalid item item_type: {item_type}")
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
        return f"{self.name} is a {self.rarity.name} item with {self.health} health, {self.damage} damage, {self.elemental_damage} elemental damage, {self.bleed_threshold_damage} bleed threshold damage, {self.resist} resist, {self.elemental_resists} elemental resists, {self.bleed_threshold} bleed threshold, {self.critical_chance} critical chance, {self.critical_damage} critical damage, {self.self_healing} self healing, {self.healing} healing, {self.autoattack_speed} autoattack speed, and {self.ability_speed} ability speed."
    def __eq__(self, other):
        if isinstance(other, item_framework):
            return self.name == other.name and self.item_type == other.item_type and self.rarity == other.rarity
        return False

def rarity_odds(level):
    if level <= 5:
        return {
            'common': 1 - 0.1,
            'uncommon': 0.09,
            'rare': 0.01,
            'epic': 0
        }
    elif level <=10:
        return {
            'common': 1 - 0.01 ,
            'uncommon': 0.09  ,
            'rare': 0.009 ,
            'epic': 0.001, 
            'legendary': 0
        }
    elif level <=15:
        return {
            'common': 1 - 0.0175 ,
            'uncommon': 0.01 ,
            'rare': 0.005 ,
            'epic': 0.00245,
            'legendary': 0.0005
        }
    elif level <=20:
        return {
            'common': 1 - 0.01,
            'uncommon': 0.01 ,
            'rare': 0.005 ,
            'epic': 0.0024,
            'legendary': 0.001
        }
    else:
        return {
            'common': 1 - 0.5,
            'uncommon': 0.39 ,
            'rare': 0.1 ,
            'epic': 0.099, 
            'legendary': 0.001
        }

def rarity_determination(level):
    odds = rarity_odds(level)
    rarity_chance = random.uniform(0,1)
    if rarity_chance < odds['common']:
        chosen_rarity = rarity.common
    elif rarity_chance < odds['common'] + odds['uncommon']:
        chosen_rarity = rarity.uncommon
    elif rarity_chance < odds['common'] + odds['uncommon'] + odds['rare']:
        chosen_rarity = rarity.rare
    elif rarity_chance < odds['common'] + odds['uncommon'] + odds['rare'] + odds['epic']:
        chosen_rarity = rarity.epic
    elif rarity_chance < odds['common'] + odds['uncommon'] + odds['rare'] + odds['epic'] + odds['legendary']: 
        chosen_rarity = rarity.legendary
    return chosen_rarity


def weapon_generation(item_name,level):
    # Load the config file
    with open(config_path) as f:
        config = json.load(f)

    # Find the item in the config file
    item_config = next((item for item in config if item["name"] == item_name), None)
    if item_config is None:
        raise ValueError(f"Item '{item_name}' not found in config file")
    
    # Create the item    
    item_type = 'weapon'
    chosen_rarity = rarity_determination(level)
    health = 0
    damage = random.randint(0, 10)*chosen_rarity.value* item_config["physical_damage_modifier"]
    elemental_damage = random.randint(0,10)*chosen_rarity.value* item_config["elemental_damage_modifier"]
    bleed_threshold_damage = random.randint(0,10)*chosen_rarity.value* item_config["bleed_damage_modifier"]
    resist = 0
    elemental_resists = 0
    bleed_threshold = 0
    critical_chance = random.uniform(0,.02)*item_config["crit_chance_modifier"]*chosen_rarity.value
    critical_damage = random.uniform(0,.02)*item_config["crit_damage_modifier"]*chosen_rarity.value
    self_healing = 0
    healing = 0
    autoattack_speed = random.random()*item_config["autoattack_speed_modifier"]*chosen_rarity.value
    ability_speed = random.randint(0,10)*item_config["ability_speed_modifier"]*chosen_rarity.value
    weapon = item_framework(item_name, chosen_rarity, health, damage, elemental_damage,
                            bleed_threshold_damage, resist, elemental_resists,
                            bleed_threshold, critical_chance, critical_damage,
                            self_healing, healing, autoattack_speed, ability_speed, item_type)
    return weapon
def armor_generation(item_name, level):
    # Load the config file
    with open(config_path) as f:
        config = json.load(f)

    # Find the item in the config file
    item_config = next((item for item in config if item["name"] == item_name), None)
    if item_config is None:
        raise ValueError(f"Item '{item_name}' not found in config file")
    
    # Create the item    
    item_type = 'armor'
    chosen_rarity = rarity_determination(level)
    health = random.randint(0, 10)*chosen_rarity.value* item_config["hp_modifier"]
    damage = 0
    elemental_damage = 0
    bleed_threshold_damage = 0
    resist = random.randint(0,10)*chosen_rarity.value* item_config["physical_resistance_modifier"]
    elemental_resists = random.randint(0,10)*chosen_rarity.value* item_config["elemental_resistance_modifier"]
    bleed_threshold = random.randint(0,10)*chosen_rarity.value* item_config["bleed_threshold_modifier"]
    critical_chance = 0
    critical_damage = 0
    self_healing = random.randint(0,10)*chosen_rarity.value* item_config["ally_healing_modifier"]
    healing = random.randint(0,10)*chosen_rarity.value* item_config["self_healing_modifier"]
    autoattack_speed = 0
    ability_speed = 0
    armor = item_framework("item_name", chosen_rarity, health, damage, elemental_damage,
                            bleed_threshold_damage, resist, elemental_resists,
                            bleed_threshold, critical_chance, critical_damage,
                            self_healing, healing, autoattack_speed, ability_speed, item_type)
    return armor
def accessory_generation(item_name, level):
    # Load the config file
    with open(config_path) as f:
        config = json.load(f)

    # Find the item in the config file
    item_config = next((item for item in config if item["name"] == item_name), None)
    if item_config is None:
        raise ValueError(f"Item '{item_name}' not found in config file")
    
    # Create the item    
    item_type = 'accessory'
    chosen_rarity = rarity_determination(level)
    health = random.randint(0, 10)*chosen_rarity.value* item_config["hp_modifier"]
    damage = random.randint(0, 10)*chosen_rarity.value* item_config["physical_damage_modifier"]
    elemental_damage = random.randint(0,10)*chosen_rarity.value* item_config["elemental_damage_modifier"]
    bleed_threshold_damage = random.randint(0,10)*chosen_rarity.value* item_config["bleed_damage_modifier"]
    resist = random.randint(0,10)*chosen_rarity.value* item_config["physical_resistance_modifier"]
    elemental_resists = random.randint(0,10)*chosen_rarity.value* item_config["elemental_resistance_modifier"]
    bleed_threshold =  random.randint(0,10)*chosen_rarity.value* item_config["bleed_threshold_modifier"]
    critical_chance = random.uniform(0,.02)*item_config["crit_chance_modifier"]
    critical_damage = random.uniform(0,.02)*item_config["crit_damage_modifier"]
    self_healing = random.randint(0,10)*chosen_rarity.value* item_config["ally_healing_modifier"]
    healing = random.randint(0,10)*chosen_rarity.value* item_config["self_healing_modifier"]
    autoattack_speed = random.random()*item_config["autoattack_speed_modifier"]
    ability_speed = random.randint(0,10)*item_config["ability_speed_modifier"]
    accessory = item_framework("item_name", chosen_rarity, health, damage, elemental_damage,
                            bleed_threshold_damage, resist, elemental_resists,
                            bleed_threshold, critical_chance, critical_damage,
                            self_healing, healing, autoattack_speed, ability_speed, item_type)
    return accessory

print(weapon_generation("Axe",25))
