import time, random, json, threading
from combat import combat_game as c
from objects.item_generation import weapon_generation, armor_generation, accessory_generation
from utils.guild_manager import GuildManager, PartyManager, ItemManager
import  os

class IdleGameplay:
    def __init__(self, game_state):
        self.game_state = game_state
        self.adventures = []
        self.reduce_duration = False

    def start_adventure(self, party,party_num):
        floor_reached, time_counter = c.combat_loop(party)
        duration = self.calculate_adventure_duration(time_counter)

        # Create a stop event for the adventure
        stop_event = threading.Event()

        # Create a new thread for the adventure
        adventure_thread = threading.Thread(target=self.adventure, args=(party,party_num, duration, floor_reached, stop_event, time_counter))

        # Add the thread and the end time to the adventures list
        self.adventures.append((adventure_thread, time.time() + duration))

        # Start the adventure thread
        adventure_thread.start()

        # Return the adventure thread
        return adventure_thread
    
   
    def calculate_adventure_duration(self, time_counter):
        
        return time_counter / 1440 #edit later

    def adventure(self, party,party_num, duration, floor_reached, stop_event, time_counter):
        # Sleep for the duration of the adventure
        while not stop_event.is_set() and duration > 0:
            #time.sleep(1)
            duration -= 1
            if self.reduce_duration:  # if the reduce_duration flag is set
                duration -= self.reduce_amount  # reduce the duration
                self.reduce_duration = False  # reset the flag

        # Calculate the rewards
        rewards = self.calculate_rewards(party, floor_reached)
        gold_reward, loot_reward = rewards
        # Add the rewards to the game state
        self.game_state['loot']['gold'] += gold_reward
        for item in loot_reward:
            ItemManager.add_item_to_inventory(self, item)


        # Print a message that the party has returned
        print(f"\n(Alert) {'guild_party_name_matrix'[party_num]} has returned from their adventure after {int(self.calculate_adventure_duration(time_counter))} days. They reached floor {floor_reached} and collected {gold_reward} gold and {len(loot_reward)} item(s).")

    def calculate_rewards(self, party, floor_reached):
        base_gold_reward = 10
        gold_increase_per_floor = 10
        gold_reward = floor_reached / 2 * (base_gold_reward + base_gold_reward + (floor_reached - 1) * gold_increase_per_floor)

        # Load items from config.json
        print(os.getcwd())
        with open('assets\\data\\config.json') as f:
            items = json.load(f)

        # Generate a random number of items based on the floor reached
        if floor_reached == 0:
            num_items = 0
        else:
            num_items = random.randint(1, 1+floor_reached//5)
        loot_reward = []
        for _ in range(num_items):
            # Choose a random item type
            item_type = random.choice(['weapon', 'armor', 'accessory'])
            # Filter items by type
            items_of_type = [item for item in items if item['type'] == item_type]
            # Choose a random item of the given type
            item = random.choice(items_of_type)

            #generate item
            if item_type == 'weapon':
                for character in party:
                    loot_reward.append(weapon_generation(item['item_name'], character.level))
            elif item_type == 'armor':
                for character in party:
                    loot_reward.append(armor_generation(item['item_name'], character.level))
            elif item_type == 'accessory':
                for character in party:
                    loot_reward.append(accessory_generation(item['item_name'], character.level))

        return (gold_reward,loot_reward)

    def check_adventures(self):
        # Print the remaining time for each adventure
        for i, (thread, end_time) in enumerate(self.adventures):
            remaining_time = max(0, end_time - time.time())
            print(f"Adventure {i + 1}: {remaining_time} seconds remaining.")

    def return_early(self, adventure_index):
        # Get the stop event for the adventure
        _, _, stop_event = self.adventures[adventure_index]

        # Set the stop event to stop the adventure
        stop_event.set()

    def reduce_adventure_duration(self, adventure_index, amount):
        # Get the adventure
        adventure = self.adventures[adventure_index]

        # Set the reduce_duration flag and the reduce_amount
        self.reduce_duration = True
        self.reduce_amount = amount

    def manager(self):
        while True:
            choice1 = input("\n1. Manage guild\n2. Manage party\n3. Manage Inventory\n4. Continue\nWhat would you like to do? ")
            if choice1 == '1':
                choice2=input("\n1. View Guild stats\n2. Move party member\n3.Remove party member\nWhat would you like to do? ")
                if choice2 == '1':
                    GuildManager.view_guild(self)
                    break
                elif choice2 == '2':
                    for a in range(int(self.game_state['guild_size'])):
                        for b in range(4):
                            if self.game_state['guild_member_matrix'][a][b] != 0:
                                print(((int(self.game_state['guild_size']))*a+1)+b, self.game_state['guild_member_matrix'][a][b].name)
                    try:
                        choice2a = input("Which party member would you like to move? ")
                        a=int(choice2a)//4
                        GuildManager.move_party_member(self, self.game_state['guild_member_matrix'][a][int(choice2a)-1-3*a])
                    except ValueError:
                        print("Invalid input.")
                        continue
                elif choice2 == '3':
                    for a in range(int(self.game_state['guild_size'])):
                        for b in range(4):
                            if self.game_state['guild_member_matrix'][a][b] != 0:
                                print(((int(self.game_state['guild_size']))*a+1)+b, self.game_state['guild_member_matrix'][a][b].name)
                    try:
                        choice2a = input("Which party member would you like to remove? ")
                        a=int(choice2a)//4
                        GuildManager.remove_party_member(self, self.game_state['guild_member_matrix'][a][int(choice2a)-1-3*a])
                    except ValueError:
                        print("Invalid input.")
                        continue
                    break
                else:
                    print("Invalid input.")
            elif choice1 == '2':
                choice3 = input("\n1. Level up party member\n2. Equip item\n3. Unequip item\n4.View party stats\nWhat would you like to do? ")
                if choice3 == '1':
                    for a in range(int(self.game_state['guild_size'])):
                        for b in range(4):
                            print({((int(self.game_state['guild_size']))*a+1)+b})
                            print(self.game_state['guild_member_matrix'][a][b].name)
                    choice3a = input("Which party member would you like to level up? ")
                    a=int(choice3a)%4
                    PartyManager.level_up(self, self.game_state['guild_member_matrix'][a][choice3a-1-3*a])
                    break
                elif choice3 == '2':
                    for a in range(int(self.game_state['guild_size'])):
                        for b in range(4):
                            print({((int(self.game_state['guild_size']))*a+1)+b})
                            print(self.game_state['guild_member_matrix'][a][b].name)
                    adventurer = input("Which party member would you like to equip? ")
                    a=int(adventurer)%4
                    for i in range(5):
                        for j in range(5):
                            print({(5*a+1)+b})
                            print(self.game_state['loot']['inventory'][i][j].name)
                    item = input("Which item would you like to equip? ")
                    i = int(item)%5
                    PartyManager.equip_item(self, self.game_state['guild_member_matrix'][a][adventurer-1-3*a], self.game_state['loot']['inventory'][i][item-1-4*i])
                    break
                elif choice3 == '3':
                    for a in range(int(self.game_state['guild_size'])):
                        for b in range(4):
                            print({((int(self.game_state['guild_size']))*a+1)+b})
                            print(self.game_state['guild_member_matrix'][a][b].name)
                    adventurer = input("Which party member would you like to unequip? ")
                    a=int(adventurer)%4
                    for i in range(5):
                        for j in range(5):
                            print({(5*a+1)+b})
                            print(self.game_state['loot']['inventory'][i][j].name)
                    item = input("Which item would you like to unequip? ")
                    i = int(item)%5
                    PartyManager.unequip_item(self, self.game_state['guild_member_matrix'][a][adventurer-1-3*a], self.game_state['loot']['inventory'][i][item-1-4*i])
                    break
                elif choice3 == '4':
                    PartyManager.view_party_stats(self)
                    break
            elif choice1 == '3':
                choice4 = input("\n1. View inventory\nWhat would you like to do? ")
                if choice4 == '1':
                    ItemManager.view_items(self)
                    break
                else:
                    print("Invalid input.")
            elif choice1 == '4':
                break
            else:
                print("Invalid input.")
            print("\nReturning to adventure...")
            break