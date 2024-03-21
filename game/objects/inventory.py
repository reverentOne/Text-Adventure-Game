import numpy
i = 5 # defines the number of rows in the inventory
j = 5 # defines the number of columns in the inventory
inventory = numpy.zeros((i,j)) # defines the global inventory as a 5x5 array of zeros
# The following functions are used to interact with the inventory
def clear_inventory(): # clears the inventory
    global inventory
    inventory = numpy.zeros((i,j))

def add_item_to_inventory(item): # adds an item to the inventory
    global inventory
    if numpy.all(inventory != 0):
        for a in range(i):
            for b in range(j):
                if inventory[a][b] == 0:
                    inventory[a][b] = item
                    return True
    else:
        print("Inventory is full.")

def remove_item_from_inventory(item):# removes an item from the inventory
    global inventory
    for a in range(i):
        for b in range(j):
            if inventory[a][b] == item:
                inventory[a][b] = 0
                return True
            else:
                print("Item not found in inventory.")
                return False

def read_inventory(): # prints the inventory
    global inventory
    for a in range(i):
        for b in range(j):
            object = inventory[a][b]
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
