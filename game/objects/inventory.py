import numpy
class InventoryManager:
    def __init__(self, game_state):
            self.game_state = game_state
    # The following functions are used to interact with the inventory
    def clear_inventory(self): # clears the inventory
        self.game_state['loot']['inventory'] = numpy.zeros((i,j))

    def add_item_to_inventory(self,item): # adds an item to the inventory
        if numpy.all(self.game_state['loot']['inventory'] != 0):
            for a in range(i):
                for b in range(j):
                    if self.game_state['loot']['inventory'][a][b] == 0:
                        self.game_state['loot']['inventory'][a][b] = item
                        return True
        else:
            print("Inventory is full.")

    def remove_item_from_inventory(self,item):# removes an item from the inventory
        
        for a in range(i):
            for b in range(j):
                if self.game_state['loot']['inventory'][a][b] == item:
                    self.game_state['loot']['inventory'][a][b] = 0
                    return True
                else:
                    print("Item not found in inventory.")
                    return False

    def read_inventory(self): # prints the inventory
        for a in range(i):
            for b in range(j):
                object = self.game_state['loot']['inventory'][a][b]
                if object != 0:
                    if object.item_type == "weapon":
                        print(f"{object.name} (Weapon) ")
                    elif object.item_type == "armor":
                        print(f"{object.name} (Armor) ")
                    elif object.item_type == "accessory":
                        print(f"{object.name} (Accessory) ")
                    else:
                        print("Empty")
                else:
                    print("Empty")
