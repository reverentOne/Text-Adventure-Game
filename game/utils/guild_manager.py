import numpy

from objects.adventurer_generation_2 import character_framework


class GuildManager:
    def __init__(self, game_state):
        self.game_state = game_state
    def guild_members(self,party_array,name): #adds a party to the guild
        for i in range(int(self.game_state['guild_size'])):
            if numpy.all(self.game_state['guild_member_matrix'][i] == 0):
                self.game_state['guild_member_matrix'][i] = party_array
                self.game_state['guild_party_name_matrix'][i] = name
                return True
            
    def move_party_member(self,character): #moves a party member to a different slot in the guild and replaces the old slot with a different party member
        for a in range(int(self.game_state['guild_size'])):
            for b in range(int(self.game_state['guild_size'])):
                if self.game_state['guild_member_matrix'][a][b] == 0: 
                    continue
                if character == self.game_state['guild_member_matrix'][a][b]:
                    found_at = (a, b)
                    self.game_state['guild_member_matrix'][a][b] = 0
                    choice = int(input("where would you like to move this party member? "))
                    replace = self.game_state['guild_member_matrix'][choice-1 -4*(choice%4)][choice%4]
                    self.game_state['guild_member_matrix'][choice-1 -4*(choice%4)][choice%4] = character
                    self.game_state['guild_member_matrix'][found_at[0]][found_at[1]] = replace
                    return True
                
    def add_party_member(self,character): #adds a character to the guild
        print("The following parties have open slots: ")
        counter = 0
        for a in range(int(self.game_state['guild_size'])):
            counter += 1
            if numpy.any(self.game_state['guild_member_matrix'][a] == 0):
                print(str(counter) + self.game_state['guild_party_name_matrix'][i] + " has an open slot.")
        i = int(input("which party member would you like to add? "))
        if not numpy.any(self.game_state['guild_member_matrix'][i] == 0):
            print("That party is full.")
            return False
        elif numpy.where(self.game_state['guild_member_matrix'][i]==0):
            zero_cell = numpy.argwhere(self.game_state['guild_member_matrix'][i] == 0)[0]
            self.game_state['guild_member_matrix'][zero_cell[0]][zero_cell[1]] = character
            return True
        
    def remove_party_member(self,character):
        for a in range(int(self.game_state['guild_size'])):
            for b in range(int(self.game_state['guild_size'])):
                if character == self.game_state['guild_member_matrix'][a][b]:
                    self.game_state['guild_member_matrix'][a][b] = 0
                    return True

class PartyManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def level_up(self, character):
        experience_amount = int(input("How much experience would you like to give this character? "))
        if experience_amount < self.game_state['loot'][character.rarity + " experience"]:
            character.experience += experience_amount
            self.game_state['loot'][character.rarity + " experience"] -= experience_amount
            return True
        else:
            print("You do not have enough experience to level up this character.")
            return False

    def equip_item(self, character, item):
        for a in range(int(self.game_state['guild_size'])):
            for b in range(int(self.game_state['guild_size'])):
                if character == self.game_state['guild_member_matrix'][a][b]:
                    character_framework.equip(character,item)
                    for a in range(5):
                        for b in range(5):
                            if self.game_state['loot']['inventory'] == item:
                                self.game_state['loot']['inventory'][a][b] = 0
                                return True
                            
    def unequip_item(self, character, item):
        for a in range(int(self.game_state['guild_size'])):
            for b in range(int(self.game_state['guild_size'])):
                if character == self.game_state['guild_member_matrix'][a][b]:
                    character_framework.unequip(character,item)
                    for a in range(5):
                        for b in range(5):
                            if self.game_state['loot']['inventory'] == 0:
                                self.game_state['loot']['inventory'][a][b] = item
                                return True

    def view_party_stats(self):
        selected_party = int(input("Which party would you like to view? "))
        for b in range(4):
            print(self.game_state['guild_member_matrix'][selected_party][b])

class ItemManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def buy_item(self, item):
        # Implement buying an item
        pass

    def sell_item(self, item):
        # Implement selling an item
        pass
    def view_items(self):
        for a in range(5):
            for b in range(5):
                object = self.game_state['loot']['inventory'][a][b]
                if object != 0:
                    if object.item_type == "weapon":
                        print(f"{object} (Weapon) ")
                    elif object.item_type == "armor":
                        print(f"{object} (Armor) ")
                    elif object.item_type == "accessory":
                        print(f"{object} (Accessory) ")
                    else:
                        print("Empty")
                else:
                    print("Empty")
class TradeManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def trade(self, offer, request):
        # Implement trading
        pass

class ProgressTracker:
    def __init__(self, game_state):
        self.game_state = game_state

    def track_progress(self):
        # Implement progress tracking
        pass