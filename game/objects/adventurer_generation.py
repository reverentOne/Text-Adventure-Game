import random
import array
import numpy
floor = 0
first_names=('James',	'John',	'Robert',	'Michael',	'William',	'David',	'Richard',	'Charles',	'Joseph',	'Thomas', 'Mary',	'Patricia',	'Linda',	'Barbara',	'Elizabeth',	'Jennifer',	'Maria',	'Susan',	'Margaret',	'Dorothy')
last_names=('Johnson','Smith','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson')


class character_framework:
    def __init__(self,name, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed):
        self.name = name
        self.health = health
        self.base_physical_damage = damage 
        self.base_elemental_damage = elemental_damage 
        self.bleed_threshold_damage = bleed_threshold_damage 
        self.physical_resistance = resist  
        self.elemental_resists = elemental_resists  
        self.bleed_threshold = bleed_threshold  
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.self_healing = self_healing
        self.ally_healing = healing
        self.attack_speed = autoattack_speed
        self.ability_speed = ability_speed
        self.rating = round(health/10 + damage + elemental_damage + bleed_threshold_damage/3 + resist/5 + elemental_resists/5 + bleed_threshold/100 + critical_chance + critical_damage + self_healing + healing + ability_speed/150)
    def __str__(self):
        return (f"{'Name': <25} {self.name:<25} {'Bleed Threshold Damage': <25} {self.bleed_threshold_damage:<25}\n"
                f"{'Health': <25} {self.health:<25} {'Bleed Threshold': <25} {self.bleed_threshold:<25}\n"
                f"{'Base Physical Damage': <25} {self.base_physical_damage:<25} {'Critical Chance': <25} {self.critical_chance:<25}\n"
                f"{'Base Elemental Damage': <25} {self.base_elemental_damage:<25} {'Critical Damage': <25} {self.critical_damage:<25}\n"
                f"{'Physical Resistance': <25} {self.physical_resistance:<25} {'Self Healing': <25} {self.self_healing:<25}\n"
                f"{'Elemental Resistance': <25} {self.elemental_resists:<25} {'Ally Healing': <25} {self.ally_healing:<25}\n"
                f"{'Attack Speed': <25} {self.attack_speed:<25} {'Ability Speed': <25} {self.ability_speed:<25}\n"
                f"{'Rating': <25} {self.rating:<25}")

def common_adventurer():
    group=random.choice(first_names)+" "+random.choice(last_names)
    level = 1
    expierence = 100*level
    exp = 0
    shard = 0
    star_level =0
    upgrade_points = 0
    name = group
    health = 10
    damage = random.randint(0, 3)
    elemental_damage = 0
    bleed_threshold_damage = 3
    resist = 5
    elemental_resists = 5
    bleed_threshold = 100
    critical_chance = 0
    critical_damage = 0
    self_healing = 0
    healing = random.randint(0,5)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,250) 
    common_adventurer = character_framework(name,health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    if exp >= expierence:
        level+=1
        upgrade_points+=5
        while upgrade_points > 0:
            input("What do you wish to upgrade? 1. health, 2. Damage, 3. Elemental Damage, 4. Conditions Damage, 5. Resistances, 6. Elemental Resistance, 7. Conditions Resistance, 8. critical striike chance, 9. critical strike damage, 10. regeneration, 11. healing, 12. attack speed, 13. ability cooldown")
            if 1:
                health +=5
                upgrade_points-=1
            elif 2:
                damage += random.randint(0,2)
                upgrade_points-=1
            elif 3:
                elemental_damage += random.randint(0,2)
                upgrade_points-=1
            elif 4:
                bleed_threshold_damage += random.randint(0,7)
                upgrade_points-=1
            elif 5:
                resist += random.randint(0,2)
                upgrade_points-=1
            elif 6:
                elemental_resists += random.randint(0,2)
                upgrade_points -= 1
            elif 7:
                bleed_threshold += random.randint(0,7)
                upgrade_points -= 1
            elif 8:
                critical_chance += .01
                upgrade_points -= 1
            elif 9:
                critical_damage += .01
                upgrade_points -= 1
            elif 10:
                self_healing += 1
                upgrade_points -= 1
            elif 11:
                healing += 5
                upgrade_points -=1
            elif 12:
                autoattack_speed +=.01
                upgrade_points -=1
            elif 13:
                ability_speed -=1
                upgrade_points -=1
            else:
                print("Type the number associated with the stat you want to upgrade.")
    if shard == 100 and star_level<5:
        health += 10
        damage += random.randint(0, 3)
        elemental_damage += 10
        bleed_threshold_damage += 10
        resist += 5
        elemental_resists += 5
        bleed_threshold += 100,100
        critical_chance += .1
        critical_damage += .1
        self_healing += 2
        healing += random.randint(0,5)
        autoattack_speed += .1
        ability_speed -= random.randint(0,15)
        shard -= 100
        star_level += 1
    return(common_adventurer)
def uncommon_adventurer():
    group=random.choice(first_names)+" "+random.choice(last_names)
    level = 1
    expierence = 250*level
    exp = 0
    shard = 0
    star_level =0
    upgrade_points = 0
    name = group
    health = 25
    damage = random.randint(0, 5)
    elemental_damage = 1
    bleed_threshold_damage = 5
    resist = 7
    elemental_resists = 7
    bleed_threshold = 125
    critical_chance = 0
    critical_damage = 0
    self_healing = 0
    healing = random.randint(0,7)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,290) 
    uncommon_adventurer = character_framework(name,health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    if exp >= expierence:
        level+=1
        upgrade_points+=5
        while upgrade_points > 0:
            input("What do you wish to upgrade? 1. health, 2. Damage, 3. Elemental Damage, 4. Conditions Damage, 5. Resistances, 6. Elemental Resistance, 7. Conditions Resistance, 8. critical striike chance, 9. critical strike damage, 10. regeneration, 11. healing, 12. attack speed, 13. ability cooldown")
            if 1:
                health +=6
                upgrade_points-=1
            elif 2:
                damage += random.randint(0,2)
                upgrade_points-=1
            elif 3:
                elemental_damage += random.randint(0,2)
                upgrade_points-=1
            elif 4:
                bleed_threshold_damage += random.randint(0,7)
                upgrade_points-=1
            elif 5:
                resist += random.randint(0,2)
                upgrade_points-=1
            elif 6:
                elemental_resists += random.randint(0,2)
                upgrade_points -= 1
            elif 7:
                bleed_threshold += random.randint(0,7)
                upgrade_points -= 1
            elif 8:
                critical_chance += .01
                upgrade_points -= 1
            elif 9:
                critical_damage += .01
                upgrade_points -= 1
            elif 10:
                self_healing += 1.1
                upgrade_points -= 1
            elif 11:
                healing += 5.2
                upgrade_points -=1
            elif 12:
                autoattack_speed +=.012
                upgrade_points -=1
            elif 13:
                ability_speed -=1
                upgrade_points -=1
            else:
                print("Type the number associated with the stat you want to upgrade.")
    if shard == 100 and star_level<5:
        health += 10
        damage += random.randint(0, 5)
        elemental_damage += 15
        bleed_threshold_damage += 10
        resist += 7
        elemental_resists += 8
        bleed_threshold += 125
        critical_chance += .1
        critical_damage += .1
        self_healing += 2
        healing += random.randint(0,7)
        autoattack_speed += .1
        ability_speed -= random.randint(0,17)
        shard -= 100
        star_level += 1
    return(uncommon_adventurer)
def rare_adventurer():
    group=random.choice(first_names)+" "+random.choice(last_names)
    level = 1
    expierence = 250*level
    exp = 0
    shard = 0
    star_level =0
    upgrade_points = 0
    name = group
    health = 25
    damage = random.randint(0, 5)
    elemental_damage = 2
    bleed_threshold_damage = 2
    resist = 9
    elemental_resists = 9
    bleed_threshold = 140
    critical_chance = 0
    critical_damage = 0
    self_healing = 0
    healing = random.randint(0,9)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,280) 
    rare_adventurer = character_framework(name, health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    if exp >= expierence:
        level+=1
        upgrade_points+=5
        while upgrade_points > 0:
            input("What do you wish to upgrade? 1. health, 2. Damage, 3. Elemental Damage, 4. Conditions Damage, 5. Resistances, 6. Elemental Resistance, 7. Conditions Resistance, 8. critical striike chance, 9. critical strike damage, 10. regeneration, 11. healing, 12. attack speed, 13. ability cooldown")
            if 1:
                health +=8
                upgrade_points-=1
            elif 2:
                damage += random.randint(0,3)
                upgrade_points-=1
            elif 3:
                elemental_damage += random.randint(0,3)
                upgrade_points-=1
            elif 4:
                bleed_threshold_damage += random.randint(0,9)
                upgrade_points-=1
            elif 5:
                resist += random.randint(0,3)
                upgrade_points-=1
            elif 6:
                elemental_resists += random.randint(0,3)
                upgrade_points -= 1
            elif 7:
                bleed_threshold += random.randint(0,9)
                upgrade_points -= 1
            elif 8:
                critical_chance += .01
                upgrade_points -= 1
            elif 9:
                critical_damage += .01
                upgrade_points -= 1
            elif 10:
                self_healing += 1.3
                upgrade_points -= 1
            elif 11:
                healing += 5.3
                upgrade_points -=1
            elif 12:
                autoattack_speed +=.013
                upgrade_points -=1
            elif 13:
                ability_speed -=1
                upgrade_points -=1
            else:
                print("Type the number associated with the stat you want to upgrade.")
    if shard == 100 and star_level<5:
        health += 15
        damage += random.randint(0, 7)
        elemental_damage += 25
        bleed_threshold_damage += 15
        resist += 9
        elemental_resists += 9
        bleed_threshold += 125
        critical_chance += .1
        critical_damage += .1
        self_healing += 3
        healing += random.randint(0,9)
        autoattack_speed += .1
        ability_speed -= random.randint(0,19)
        shard -= 100
        star_level += 1
    return(rare_adventurer)
def epic_adventurer():
    group=random.choice(first_names)+" "+random.choice(last_names)
    level = 1
    expierence = 400*level
    exp = 0
    shard = 0
    star_level =0
    upgrade_points = 0
    name = group
    health = 40
    damage = random.randint(0, 7)
    elemental_damage = 3
    bleed_threshold_damage = 5
    resist = 12
    elemental_resists = 12
    bleed_threshold = 150
    critical_chance = 0
    critical_damage = 0
    self_healing = 0
    healing = random.randint(0,12)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,260) 
    epic_adventurer = character_framework(name, health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    if exp >= expierence:
        level+=1
        health+=9
        upgrade_points+=5
        while upgrade_points > 0:
            input("What do you wish to upgrade? 1. health, 2. Damage, 3. Elemental Damage, 4. Conditions Damage, 5. Resistances, 6. Elemental Resistance, 7. Conditions Resistance, 8. critical striike chance, 9. critical strike damage, 10. regeneration, 11. healing, 12. attack speed, 13. ability cooldown")
            if 1:
                health +=10
                upgrade_points-=1
            elif 2:
                damage += random.randint(0,5)
                upgrade_points-=1
            elif 3:
                elemental_damage += random.randint(0,5)
                upgrade_points-=1
            elif 4:
                bleed_threshold_damage += random.randint(0,12)
                upgrade_points-=1
            elif 5:
                resist += random.randint(0,5)
                upgrade_points-=1
            elif 6:
                elemental_resists += random.randint(0,5)
                upgrade_points -= 1
            elif 7:
                bleed_threshold += random.randint(0,12)
                upgrade_points -= 1
            elif 8:
                critical_chance += .02
                upgrade_points -= 1
            elif 9:
                critical_damage += .02
                upgrade_points -= 1
            elif 10:
                self_healing += 1.5
                upgrade_points -= 1
            elif 11:
                healing += 5.5
                upgrade_points -=1
            elif 12:
                autoattack_speed +=.015
                upgrade_points -=1
            elif 13:
                ability_speed -=1.5
                upgrade_points -=1
            else:
                print("Type the number associated with the stat you want to upgrade.")
    if shard == 100 and star_level<5:
        health += 40
        damage += random.randint(0, 12, size=(1, 3))
        elemental_damage += 25
        bleed_threshold_damage += 35
        resist += 25
        elemental_resists += 25
        bleed_threshold += 150
        critical_chance += .1
        critical_damage += .1
        self_healing += 5
        healing += random.randint(0,14)
        autoattack_speed += .1
        ability_speed -= random.randint(0,25)
        shard -= 100
        star_level += 1
    return(epic_adventurer)
def legendary_adventurer():
    group=random.choice(first_names)+" "+random.choice(last_names)
    level = 1
    expierence = 500*level
    exp = 0
    shard = 0
    star_level =0
    upgrade_points = 0
    name = group
    health = 50
    damage = random.randint(0, 12)
    elemental_damage = 5
    bleed_threshold_damage = 8
    resist = 18
    elemental_resists = 18
    bleed_threshold = 250
    critical_chance = .05
    critical_damage = .05
    self_healing = 2
    healing = random.randint(0,25)
    autoattack_speed = random.random()
    ability_speed = random.randint(0,250) 
    legendary_adventurer = character_framework(name, health, damage,elemental_damage,
                                     bleed_threshold_damage, resist, elemental_resists,
                                     bleed_threshold,critical_chance, critical_damage,
                                       self_healing, healing, autoattack_speed, ability_speed)
    if exp >= expierence:
        level+=1
        upgrade_points+=5
        while upgrade_points > 0:
            input("What do you wish to upgrade? 1. health, 2. Damage, 3. Elemental Damage, 4. Conditions Damage, 5. Resistances, 6. Elemental Resistance, 7. Conditions Resistance, 8. critical striike chance, 9. critical strike damage, 10. regeneration, 11. healing, 12. attack speed, 13. ability cooldown")
            if 1:
                health +=12
                upgrade_points-=1
            elif 2:
                damage += random.randint(0,8)
                upgrade_points-=1
            elif 3:
                elemental_damage += random.randint(0,8)
                upgrade_points-=1
            elif 4:
                bleed_threshold_damage += random.randint(0,25)
                upgrade_points-=1
            elif 5:
                resist += random.randint(0,8)
                upgrade_points-=1
            elif 6:
                elemental_resists += random.randint(0,8)
                upgrade_points -= 1
            elif 7:
                bleed_threshold += random.randint(0,25)
                upgrade_points -= 1
            elif 8:
                critical_chance += .03
                upgrade_points -= 1
            elif 9:
                critical_damage += .03
                upgrade_points -= 1
            elif 10:
                self_healing += 2
                upgrade_points -= 1
            elif 11:
                healing += 7
                upgrade_points -=1
            elif 12:
                autoattack_speed +=.03
                upgrade_points -=1
            elif 13:
                ability_speed -=2
                upgrade_points -=1
            else:
                print("Type the number associated with the stat you want to upgrade.")
    if shard == 100 and star_level<5:
        health += 80
        damage += random.randint(0, 25)
        elemental_damage += 35
        bleed_threshold_damage += 40
        resist += 25,25,25
        elemental_resists += 25
        bleed_threshold += 250
        critical_chance += .1
        critical_damage += .1
        self_healing += 5
        healing += random.randint(0,25)
        autoattack_speed += .1
        ability_speed -= random.randint(0,25)
        shard -= 100
        star_level += 1
    return(legendary_adventurer)