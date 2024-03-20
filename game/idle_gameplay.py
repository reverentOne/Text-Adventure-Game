import time, random, json, threading
from combat import combat_game as c
from objects.item_generation import weapon_generation, armor_generation, accessory_generation

class IdleGameplay:
    def __init__(self, game_state):
        self.game_state = game_state
        self.adventures = []
        self.reduce_duration = False

    def start_adventure(self, party):
        floor_reached, time_counter = c.combat_loop(party)
        duration = self.calculate_adventure_duration(time_counter)

        # Create a stop event for the adventure
        stop_event = threading.Event()

        # Create a new thread for the adventure
        adventure_thread = threading.Thread(target=self.adventure, args=(party, duration, floor_reached, stop_event, time_counter))

        # Add the thread and the end time to the adventures list
        self.adventures.append((adventure_thread, time.time() + duration))

        # Start the adventure thread
        adventure_thread.start()

        # Return the adventure thread
        return adventure_thread

    def calculate_adventure_duration(self, time_counter):
        
        return time_counter / 1440 #edit later

    def adventure(self, party, duration, floor_reached, stop_event, time_counter):
        # Sleep for the duration of the adventure
        while not stop_event.is_set() and duration > 0:
            time.sleep(1)
            duration -= 1
            if self.reduce_duration:  # if the reduce_duration flag is set
                duration -= self.reduce_amount  # reduce the duration
                self.reduce_duration = False  # reset the flag

        # Calculate the rewards
        rewards = self.calculate_rewards(party, floor_reached)

        # Add the rewards to the game state
        self.game_state['loot']['gold'] += rewards['gold']
        self.game_state['loot']['items'].append(rewards['loot'])

        # Print a message that the party has returned
        print(f"{party.name} has returned from their adventure after {int(self.calculate_adventure_duration(time_counter))} days. They reached floor {floor_reached} and collected {rewards['gold']} gold and {len(rewards['loot'])} item(s).")

    def calculate_rewards(self, party, floor_reached):
        base_gold_reward = 10
        gold_increase_per_floor = 10
        gold_reward = floor_reached / 2 * (base_gold_reward + base_gold_reward + (floor_reached - 1) * gold_increase_per_floor)

        # Load items from config.json
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
                loot_reward.append(weapon_generation(item['name'], party.level))
            elif item_type == 'armor':
                loot_reward.append(armor_generation(item['name'], party.level))
            elif item_type == 'accessory':
                loot_reward.append(accessory_generation(item['name'], party.level))

        return {"gold": gold_reward, "loot": loot_reward}

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