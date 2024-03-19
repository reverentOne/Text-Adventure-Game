

class party:
    def __init__(self, name, members, inventory, level, experience):
        self.name = name
        self.members = members
        self.inventory = inventory
        self.level = level
        self.experience = experience

    def add_to_party(self, character):
        self.members.append(character)

    def remove_from_party(self, character):
        self.members.remove(character)

    def weakest_adventurer(self):
        return min(self.members, key=lambda x: x.health)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]

    def __iter__(self):
        return iter(self.members)

    def __repr__(self):
        return f"{self.members}"