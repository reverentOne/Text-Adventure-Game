import sys
import pathlib
# Get the root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
import pygame
import numpy
from game_ui.buttons import clickable_lists
from game_ui.text import text_box
from game_ui.screen_manager import run_screen
from objects.char_gen import CharacterGenerator


class GuildManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def view_guild(self, screen):
        pygame.init()
        font = pygame.font.SysFont("Arial", 24)

        # Create a clickable list for guild names
        guild_list = clickable_lists(font, 50, 50, 200, 50)  # x, y, width, height of each item
        for guild_name, _ in self.game_state['guild_teams']:
            guild_list.add_option(guild_name)  # Add each guild name to the clickable list

        batch = [guild_list]

        # Use run_screen to select a guild
        selected_guild = run_screen(screen, batch, [guild_list], lambda guild: guild)

        # Debug: Check if a guild was selected
        if not selected_guild:
            print("No guild selected.")
            return

        print(f"Selected guild: {selected_guild}")

        # Find the corresponding team
        member_boxes = []
        for name, team in self.game_state['guild_teams']:
            if name == selected_guild:
                print(f"Team found for guild: {name}")
                # Create text boxes for each member
                for i, member in enumerate(team):
                    x, y = 300, 50 + i * 50  # Position for each member textbox
                    text = member.name if member != 0 else "Empty"
                    member_box = text_box(x, y, 300, 50, True, text, True, font)
                    member_boxes.append(member_box)

        # Add member boxes to the batch
        batch.extend(member_boxes)

        # Render the updated batch with member boxes
        run_screen(screen, batch)

        pygame.quit()
    
    def guild_members(self, party, name): #adds a party to the guild
        self.game_state['guild_teams'].append((name, party))
        return
            
    def move_party_member(self, screen, character): 
        pygame.init()
        font = pygame.font.SysFont("Arial", 24)
        running = True
        batch = []
        # Create a clickable list for guild names
        guild_list = clickable_lists(font, 50, 50, 200, 40)  # x, y, width, height of each item
        for guild_name, _ in self.game_state['guild_teams']:
            guild_list.add_option(guild_name)  # Add each guild name to the clickable list
        batch.append(guild_list)

        # Use run_screen to select a guild
        selected_guild = run_screen(screen, batch, [guild_list], lambda guild: guild)

        # Find the corresponding team and add the character
        if selected_guild:
            for name, team in self.game_state['guild_teams']:
                if name == selected_guild:
                    team.append(character)  # Add the character to the selected team
                    break

        
        
                
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

   
"""class PartyManager:
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
        else: #This doesn't work with how the adventure is set up. The thread finishes before the user can replace an item
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
                return False

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
        return
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
        pass"""

