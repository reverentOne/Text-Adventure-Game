import numpy

from objects.adventurer_generation_2 import character_framework


class GuildManager:
    def __init__(self, game_state):
        self.game_state = game_state
    def view_guild(self):
        for i in range(int(self.game_state['guild_size'])):
            if numpy.all(self.game_state['guild_member_matrix'][i] == 0):
                print()
                print("Empty Party")
            else:
                print()
                print(self.game_state['guild_party_name_matrix'][i])
            for j in range(4):
                if self.game_state['guild_member_matrix'][i][j] == 0:
                    print("Empty")
                else:
                    print()
                    print(self.game_state['guild_member_matrix'][i][j])
    def guild_members(self,party_array,name): #adds a party to the guild
        for i in range(int(self.game_state['guild_size'])):
            if numpy.all(self.game_state['guild_member_matrix'][i] == 0):
                self.game_state['guild_member_matrix'][i] = party_array
                self.game_state['guild_party_name_matrix'][i] = name
                return True
            
    def move_party_member(self,character): #moves a party member to a different slot in the guild and replaces the old slot with a different party member
        for a in range(int(self.game_state['guild_size'])):
            for b in range(4):
                if self.game_state['guild_member_matrix'][a][b] == 0: 
                    continue
                if character == self.game_state['guild_member_matrix'][a][b]:
                    found_at = (a, b)
                    self.game_state['guild_member_matrix'][a][b] = 0
                    choice = int(input("where would you like to move this party member? "))
                    a = int(choice)//4
                    replace = self.game_state['guild_member_matrix'][a][int(choice)-1-3*a]
                    self.game_state['guild_member_matrix'][a][int(choice)-1-3*a] = character
                    self.game_state['guild_member_matrix'][found_at[0]][found_at[1]] = replace
                    print("Done")
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
    def add_item_to_inventory(self, item): # adds an item to the inventory
        added = False
        for a in range(5):
            if added == True:
                break
            for b in range(5):
                if self.game_state['loot']['inventory'][a][b] == 0:
                    self.game_state['loot']['inventory'][a][b] = item
                    added = True
                    return True
            else:
                continue
        """else: #This doesn't work with how the adventure is set up. The thread finishes before the user can replace an item
            print("Inventory is full.")
            replacement = input("Would you like to replace an item? (Y/N) ")
            if replacement == 'Y' or replacement == 'y':
                for a in range(5):
                    for b in range(5):
                        print(4*a+b+1)
                        print(self.game_state['loot']['inventory'][a][b])
                        print("\n")
                item_to_replace = input("Which item would you like to replace? ")
                i = int(item_to_replace)%5
                self.game_state['loot']['inventory'][i][item_to_replace-1-4*i] = item
                return True
            else:
                return False"""

    def view_items(self):
        for a in range(5):
            for b in range(5):
                print(5*a+b+1)
                object = self.game_state['loot']['inventory'][a][b]
                if object != 0:
                    print(object)
                    print("\n")
                else:
                    print("Empty")
                    print("\n")

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