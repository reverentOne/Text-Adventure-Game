from enum import Enum
import json

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    ACCESSORY = "accessory"


class Items:
    def __init__(self, name, type, physical_damage_modifier, elemental_damage_modifier, physical_resistance_modifier,
                 elemental_resistance_modifier, bleed_threshold_modifier, bleed_damage_modifier, crit_chance_modifier,
                 crit_damage_modifier, ally_healing_modifier, self_healing_modifier, hp_modifier):
        type = ItemType(type)
        if type not in ItemType:
            raise ValueError(f"Invalid item type: {type}")
        self.name = name
        self.type = type
        self.physical_damage_modifier = physical_damage_modifier
        self.elemental_damage_modifier = elemental_damage_modifier
        self.physical_resistance_modifier = physical_resistance_modifier
        self.elemental_resistance_modifier = elemental_resistance_modifier
        self.bleed_threshold_modifier = bleed_threshold_modifier
        self.bleed_damage_modifier = bleed_damage_modifier
        self.crit_chance_modifier = crit_chance_modifier
        self.crit_damage_modifier = crit_damage_modifier
        self.ally_healing_modifier = ally_healing_modifier
        self.self_healing_modifier = self_healing_modifier
        self.hp_modifier = hp_modifier

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}"

    def __eq__(self, other):
        if isinstance(other, Items):
            return self.name == other.name and self.type == other.type
        return False

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    @classmethod
    def get_item_data_by_name(cls, name):
        with open('config.json', 'r') as f:
            data = json.load(f)
        return cls.from_json(next(item for item in data if item["name"] == name))
    
"""Debugging"""
sword = Items.get_item_data_by_name("Short Sword")
print(sword)
Big_Ham = Items.get_item_data_by_name("Hammer")
print(Big_Ham)