class CharacterGenerator:
    def __init__(self):
        self.unique_character_data = {
            "name":"",
            "level": 1,
            "rating": 0
        }
        self.base_character_data = {
            "health": 0,

        }
        self.equipment = {}
        self.attacks = []
    
    