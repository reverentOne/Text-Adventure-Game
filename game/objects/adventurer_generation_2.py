import random
import numpy

rarity_multiplier = {
    'common': 1 ,
    'uncommon': 2,
    'rare': 3,
    'epic': 4,
    'legendary': 5
}
class character_framework:
    first_names=('James',	'John',	'Robert',	'Michael',	'William',	'David',	'Richard',	'Charles',	'Joseph',	'Thomas', 'Mary',	'Patricia',	'Linda',	'Barbara',	'Elizabeth',	'Jennifer',	'Maria',	'Susan',	'Margaret',	'Dorothy')
    last_names=('Johnson','Smith','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson')


    def rarity_chance(self):
        chance = random.uniform(1,100)
        if chance <= 75:
            return 'common'
        elif chance <= 85:
            return 'uncommon'
        elif chance <= 95:
            return 'rare'
        elif chance <= 99.8:
            return 'epic'
        else:
            return 'legendary'
        
    def __init__(self,name,level,experience_requirements,experience, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed):
        self.name = name
        self.level = level
        self.experience_requirements = experience_requirements
        self.experience = experience
        self.star_shards = 0
        self.star = 0
        self.status = None
        self.equipment_slots_types = numpy.array(['weapon','armor','accessory']) #types of equipment in slots can be expanded
        self.equipment_slots = numpy.array([None,None,None]) #slots for equipment
        self.rarity = None
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
        self.unique_nature = None
        self.rating = round(health/10 + damage + elemental_damage + bleed_threshold_damage/3 + resist/5 + elemental_resists/5 + bleed_threshold/100 + critical_chance + critical_damage + self_healing + healing + ability_speed/150)
        self.attribute_matrix = numpy.array([[health, damage, elemental_damage], 
                                    [bleed_threshold_damage, resist, elemental_resists],
                                    [bleed_threshold, critical_chance, critical_damage],
                                    [self_healing, healing, autoattack_speed],
                                    [ability_speed,0,0]])

    def __str__(self):
        return (f"{'Name': <25} {self.name:<25} {'Bleed Threshold Damage': <25} {self.bleed_threshold_damage:<25}\n"
                f"{'Health': <25} {self.health:<25} {'Bleed Threshold': <25} {self.bleed_threshold:<25}\n"
                f"{'Base Physical Damage': <25} {self.base_physical_damage:<25} {'Critical Chance': <25} {self.critical_chance:<25}\n"
                f"{'Base Elemental Damage': <25} {self.base_elemental_damage:<25} {'Critical Damage': <25} {self.critical_damage:<25}\n"
                f"{'Physical Resistance': <25} {self.physical_resistance:<25} {'Self Healing': <25} {self.self_healing:<25}\n"
                f"{'Elemental Resistance': <25} {self.elemental_resists:<25} {'Ally Healing': <25} {self.ally_healing:<25}\n"
                f"{'Attack Speed': <25} {self.attack_speed:<25} {'Ability Speed': <25} {self.ability_speed:<25}\n"
                f"{'Rating': <25} {self.rating:<25}")

    nature_attributes = numpy.array([
        [random.randint(0,5),random.randint(0,5),random.randint(0,5)],
        [random.randint(0,5),random.randint(0,5),random.randint(0,5)],
        [random.randint(0,5),random.randint(0,5),random.randint(0,5)],
        [random.randint(0,5),random.randint(0,5),random.randint(0,5)],
        [random.randint(-5,0),0,0]
        ]) #creates unique attributes increases if the character is unique

    def unique(self):
        chance = random.uniform(1,100)
        if chance <= 5:
            status = 'unique' #5% chance of being unique

    def equiping(self, item): #equips an item. I'm not sure if i can call the item_matrix from the item class or iff i need to define it in the weapon generation
        if item.item_type in self.equipment_slots_types:
            self.equipment_slots[self.equipment_slots_types.index(item.item_type)] = item
            item_attributes_matrix = item.item_matrix
            self.attribute_matrix += item_attributes_matrix
        else:
            print(f"{item.item_type} is not a valid item type")

    def unequiping(self, item):
        if item in self.equipment_slots:
            self.equipment_slots[self.equipment_slots.index(item)] = None
            item_attributes_matrix = item.item_matrix
            self.attribute_matrix -= item_attributes_matrix
        else:
            print(f"{item} is not equipped")
    def __lt__(self, other):
        return self.attack_speed < other.attack_speed
    

        

    
def character():
    rarity = character_framework.rarity_chance(character_framework)
    name = random.choice(character_framework.first_names) + ' ' + random.choice(character_framework.last_names)
    level = 1
    experience_requirements = 100*int(rarity_multiplier[rarity])*level
    experience = 0
    star_shards = 0
    star = 0
    health = 10*int(rarity_multiplier[rarity])
    damage = random.randint(1,10)*int(rarity_multiplier[rarity])
    elemental_damage = random.randint(1,2)*rarity_multiplier[rarity]
    bleed_threshold_damage = random.randint(1,5)*int(rarity_multiplier[rarity])
    resist = random.randint(1,5)*int(rarity_multiplier[rarity])
    elemental_resists = random.randint(1,5)*int(rarity_multiplier[rarity])
    bleed_threshold = random.randint(1,100)*int(rarity_multiplier[rarity])
    critical_chance = round(random.uniform(0,0.01)*int(rarity_multiplier[rarity]),3)
    critical_damage = round(random.uniform(0,0.01)*int(rarity_multiplier[rarity]),3)
    self_healing = random.randint(1,2)*int(rarity_multiplier[rarity])
    healing = random.randint(1,2)*int(rarity_multiplier[rarity])
    autoattack_speed = round(random.uniform(0,1),2)
    ability_speed = (300/int(rarity_multiplier[rarity]))
    character_matrix = numpy.array([[health, damage, elemental_damage], 
                                    [bleed_threshold_damage, resist, elemental_resists],
                                    [bleed_threshold, critical_chance, critical_damage],
                                    [self_healing, healing, autoattack_speed],
                                    [ability_speed,0,0]]) #makes a matrix of the characters attributes
    if character_framework.unique(character_framework) == 'unique':
        character_matrix += character_framework.nature_attributes(character_framework) #adds unique attributes if the character is unique
    character = character_framework(name,level,experience_requirements,experience, health, damage,elemental_damage,bleed_threshold_damage, resist, elemental_resists,bleed_threshold,
                 critical_chance, critical_damage, self_healing, healing,autoattack_speed,ability_speed)
    if experience >= experience_requirements: #level up not sure if this works or if it needs to be in another function
        level_up_points = 5
        level_up_matrix = numpy.array([
                            [random.randint(1,15),random.randint(1,3),random.randint(1,3)], 
                            [random.randint(1,3),random.randint(1,3),random.randint(1,3)],
                            [random.randint(10,20),random.uniform(0,.01),random.uniform(0,.01)],
                            [random.randint(0,2),random.randint(0,2),random.uniform(0,0.01)],
                            [random.randint(-5,0),0,0]])
        while level_up_points > 0:
            experience_requirements +=20*rarity_multiplier[rarity]
            print("1. Health")
            print("2. Base Physical Damage")
            print("3. Base Elemental Damage")
            print("4. Bleed Threshold Damage")
            print("5. Physical Resistance")
            print("6. Elemental Resistance")
            print("7. Bleed Threshold")
            print("8. Critical Chance")
            print("9. Critical Damage")
            print("10. Self Healing")
            print("11. Ally Healing")
            print("12. Attack Speed")
            print("13. Ability Speed")
            while level_up_points > 0:
                print(f"You have {level_up_points} points left to spend")
                for i in range(0,level_up_points):
                    choice = int(input("What would you like to level up? "))
                    level_up_points_matrix = numpy.array([
                                                [0,0,0], 
                                                [0,0,0],
                                                [0,0,0],
                                                [0,0,0],
                                                [0,0,0]])
                    column = choice%3
                    row = choice-1 -3*column
                    level_up_points_matrix[row][column] += level_up_matrix[row][column]
                    level_up_points -= 1
        character_matrix += level_up_points_matrix
    while star_shards > 100 and star < 5: #star up not sure if this works or if it needs to be in another function
        star_shards = 0
        star += 1
        character_matrix += numpy.array([
            [10*int(rarity_multiplier[rarity]), 2*int(rarity_multiplier[rarity]), 2*int(rarity_multiplier[rarity])],
            [2*int(rarity_multiplier[rarity]) , 2*int(rarity_multiplier[rarity]), 2*int(rarity_multiplier[rarity])],
            [10*int(rarity_multiplier[rarity]), .01*int(rarity_multiplier[rarity]), .01*int(rarity_multiplier[rarity])],
            [-3*int(rarity_multiplier[rarity]),0,0]]) #not sure if this matrix addition works or if I need to first convert the original attributes into a matrix
    level+=1
    return character
print(character())