import numpy
import drafting_party
class GuildManager:
    guild_size = 3
    guild_member_matrix = numpy.zeros((4,guild_size))

    def guild_members(self,party_array): #adds a party to the guild
        for i in range(GuildManager.guild_size):
            if numpy.all(GuildManager.guild_member_matrix[i] == 0):
                GuildManager.guild_member_matrix[i] = party_array
                return True
            
    def move_party_member(self,character): #moves a party member to a different slot in the guild and replaces the old slot with a different party member
        for a in range(GuildManager.guild_size):
            for b in range(GuildManager.guild_size):
                if GuildManager.guild_member_matrix[a][b] == 0: 
                    continue
                if character == GuildManager.guild_member_matrix[a][b]:
                    GuildManager.guild_member_matrix[a][b] = 0
                    choice = int(input("where would you like to move this party member? "))
                    replace = GuildManager.guild_member_matrix[choice-1 -4*(choice%4)][choice%4]
                    GuildManager.guild_member_matrix[choice-1 -4*(choice%4)][choice%4] = character
                    if numpy.count_nonzero(GuildManager.guild_member_matrix[a]) == 3:
                        zero_cell = numpy.where(GuildManager.guild_member_matrix[a] == 0)
                        if zero_cell[0].size > 0:
                            GuildManager.guild_member_matrix[a][zero_cell[0][0]] = replace
                            return True





        

class PartyManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def level_up(self, character):
        # Implement leveling up a character

    def equip_item(self, character, item):
        # Implement equipping an item to a character

    def view_party_stats(self):
        # Implement viewing the stats of the party

    def recruit_adventurer(self, adventurer):
        # Implement recruiting a new adventurer to the party

    def dismiss_adventurer(self, adventurer):
        # Implement dismissing an adventurer from the party

class ItemManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def buy_item(self, item):
        # Implement buying an item

    def sell_item(self, item):
        # Implement selling an item

class TradeManager:
    def __init__(self, game_state):
        self.game_state = game_state

    def trade(self, offer, request):
        # Implement trading

class ProgressTracker:
    def __init__(self, game_state):
        self.game_state = game_state

    def track_progress(self):
        # Implement progress tracking