import random
from objects.adventurer_generation import character_framework
import numpy
boss_first_name = """ "Thuzuxeith", "Peercanam", "Lisantam","Dorlgughix",
"Sezelcolchung", "Sustuthoseb", "Cablithrum",
"Dwepazam", "Abrex", "Boblirchu","Sustuthoseb", 
"Cablithrum", "Dwepazam", "Abrex", "Boblirchu", "Corgam", "Felgun", "Daenalgras", 
"Bakaeel", "Kabammam", "Muslaam al-Naasooq", "Hudhaas" """
boss_title = """ the Unyielding", "the Unbreakable", "the Unstoppable", "the Unbeatable",
 "the Unconquerable", "the Unassailable", "the Unshakeable", "the Unassailable", 
"the Unshakable", "the Unfathomable", "the Unfailing", 
"the Unfaltering", "the Unflinching", "the Unforgiving",
 "the world eater", "the destroyer", "the conqueror",
"the invincible", "the indomitable", "the insurmountable", "the first flame", 
"first among eqauls", "the last hope", "the last stand", "the last bastion" """

enemy_first_name = """ "grog", "thug", "mug", "bug", "lug", "dug", "rug", "tug", "pug", 
"jug", "fug", "zug", "vug", "cug", "xug", "yug", 
"nug", "wug", "qug, "drazkir","turt", "brodd","dart" """

def boss_enemy_generator(floor):
    name = random.choice(boss_first_name) + random.choice(boss_title)
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
    boss_enemy = character_framework(name,health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return boss_enemy
def enemy_generator(floor):
    name = random.choice(enemy_first_name)
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
    enemy = character_framework(name,health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    return enemy

def enemy_list(floor):
    enemy_party = []
    if floor % 5 == 0 and floor != 0:
        enemy_party.append(boss_enemy_generator(floor))
    else:
      for i in range(random.randint(1, 5)):
          enemy_party.append(enemy_generator(floor))
    return numpy.array(enemy_party)