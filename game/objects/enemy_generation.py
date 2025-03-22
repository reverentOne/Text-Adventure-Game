import random
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
    pass

def enemy_generator(floor):
    pass

def enemy_list(floor):
    enemy_party = []
    if floor % 5 == 0 and floor != 0:
        enemy_party.append(boss_enemy_generator(floor))
    else:
      for i in range(random.randint(1, 5)):
          enemy_party.append(enemy_generator(floor))
    return numpy.array(enemy_party)