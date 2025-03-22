import sys
import pathlib

# Get the root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
import random
import numpy
import pygame
import threading
from utils.guild_manager import GuildManager
from objects.party import party
from objects.char_gen import CharacterGenerator
from game_ui.buttons import clickable_lists
from game_ui.text import text_box
from game_ui.ui import update_display, set_up_background
from game_ui.screen_manager import run_screen

# Initialize Pygame


# draft a single character
def draft_character(screen, callback):
    pygame.init()
    traits = []
    click_loop = clickable_lists(pygame.font.SysFont("comic sans", 18), 300, 150, 200, 50)
    textbox = text_box(300, 50, 300, 50, True, "Pick your adventurer!")
    adventurers_draft_list = []
    for i in range(3):
        gen = CharacterGenerator()
        new_adventurer = gen.generate()
        adventurers_draft_list.append(new_adventurer.name)
        click_loop.add_option(str(new_adventurer.name))
        attributes = text_box(50 + (200*i + 200), 250, 200, 50, True, str(new_adventurer), True, pygame.font.SysFont("comic sans", 12))
        traits.append(attributes)
    
    batch = []
    batch.append(click_loop)
    batch.append(textbox)
    for item in traits:
        batch.append(item)
    run_screen(screen, batch, [click_loop], callback)

def draft_party(game_state, screen):
    batch = []
    textbox = text_box(300, 50, 50, 50, True, "Name Your Party")
    write = text_box(300, 150, 50, 50, False)
    batch.append(textbox)
    batch.append(write)
    name = run_screen(screen, batch, [textbox, write], lambda text: setattr(sys.modules[__name__], 'name', text))
    
    party = []
    for i in range(4):
        draft_character(screen, lambda adventurer: party.append(adventurer))
    new_party = GuildManager(game_state)
    new_party.guild_members(party, name)
    return party

