import random
class CharacterGenerator:

    first_names=('James',	'John',	'Robert',	'Michael',	'William',	'David',	'Richard',	'Charles',	'Joseph',	'Thomas', 'Mary',	'Patricia',	'Linda',	'Barbara',	'Elizabeth',	'Jennifer',	'Maria',	'Susan',	'Margaret',	'Dorothy')
    last_names=('Johnson','Smith','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson')

    rarity_mods = {
    'common': 1 ,
    'uncommon': 2,
    'rare': 3,
    'epic': 4,
    'legendary': 5
    }

    def __init__(self):
        self.name = ""
        self.rarity = ""
        self.level = 1
        self.exp = 0
        self.equipment = []
        self.attacks = []
        self.hp = 0
        self.ad = 0
        self.ap = 0
        self.armor = 0
        self.resist = 0
        self.regen = 0
        self.crit = 0
        self.speed = 0
        self.rating = 0

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

    def equip(self, item):
        if len(self.equipment) < 3:
            self.equipment.append(item)

            for attr in vars(item):
                if hasattr(self, attr) and isinstance(getattr(item, attr), (int, float)):
                    setattr(self, attr, getattr(self, attr) + getattr(item, attr))
        else:
            print(f"Cannot equip more than 3 items.")

    def unequiping(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            for attr in vars(item):
                if hasattr(self, attr) and isinstance(getattr(item, attr), (int, float)):
                    setattr(self, attr, getattr(self, attr) - getattr(item, attr))
        else:
            print(f"{item.name} is not equipped.")

    def __lt__(self, other):
        return self.speed < other.speed
    
    def __str__(self):
        attributes = ['hp', 'ad', 'ap', 'armor', 'resist', 'regen', 'crit', 'speed']
        attr_values = "".join(f"{attr}: {getattr(self, attr)}\n" for attr in attributes)
        return f"Name: {self.name}\nRarity: {self.rarity}\nRating: {self.rating:}\nLevel: {self.level}\nExp: {self.exp}\n{attr_values}"

    def generate(self):
        self.name = random.choice(self.first_names) + ' ' + random.choice(self.last_names)
        self.rarity = self.rarity_chance()
        rarity_mod = self.rarity_mods[self.rarity]
        attributes = ['hp', 'ad', 'ap', 'armor', 'resist', 'regen', 'crit', 'speed']
        
        # Generate random values for each attribute
        for attr in attributes:
            setattr(self, attr, random.randint(1, 10) * rarity_mod)
        
        # Calculate the rating as the average of all attributes
        self.rating = int(sum(getattr(self, attr) for attr in attributes) / len(attributes))
        return self
