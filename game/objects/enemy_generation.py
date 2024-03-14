import random
import array
import numpy
floor = 0
class character_framework:
    def __init__(self, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed):
        self.health = health
        self.damage = damage  # Array for slashing, piercing, bludgeoning damage
        self.elemental_damage = elemental_damage # Array for fire, radiant, and necrotic damage
        self.bleed_threshold_damage = bleed_threshold_damage # Array for poison and bleed_threshold damage
        self.resist = resist  # Array for slashing, piercing, bludgeoning resist
        self.elemental_resists = elemental_resists  # Array for fire, radiant, necrotic resists
        self.bleed_threshold = bleed_threshold  #Array for thresholds for poison and bleed_threshold
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.self_healing = self_healing
        self.healing = healing
        self.autoattack_speed = autoattack_speed
        self.ability_speed = ability_speed

def boss_enemy_generation():
    boss_enemy = character_framework
    health = random.randint(10, floor * 100 + 10)
    damage = random.randint(0, 3 * floor + 10)
    elemental_damage = random.randint(0,2*floor+8)
    bleed_threshold_damage = random.randint(0,200)
    resist = random.randint(0, 8 + 2 * floor)
    elemental_resists = random.randint(0, 35 + floor)
    bleed_threshold = random.randint(200,1000)
    critical_chance = random.random()
    critical_damage = random.random()
    self_healing = random.randint(0,10)
    healing = random.randint(0,5)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,300) 
    boss_enemy = character_framework(health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
def enemy_generation():
    enemy = character_framework
    health = random.randint(10, floor * 10 + 10)
    damage = random.randint(0, 3 * floor)
    elemental_damage = random.randint(0,floor+1)
    bleed_threshold_damage = random.randint(0,10)
    resist = random.randint(0, 8 + floor)
    elemental_resists = random.randint(0, 5 + floor)
    bleed_threshold = random.randint(200,400)
    critical_chance = random.random() - .2
    critical_damage = random.random() - .3
    self_healing = random.randint(0,1)
    healing = random.randint(0,1)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,150)
    enemy = character_framework(health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)

