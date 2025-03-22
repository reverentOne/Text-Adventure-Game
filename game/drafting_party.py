import sys
import pathlib

# Get the root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
import random
import numpy
import pygame
import threading
from utils.guild_manager import GuildManager
from objects.party import party
from objects.adventurer_generation_2 import character
from game_ui.buttons import clickable_lists
from game_ui.text import text_box
from game_ui.ui import update_display, set_up_background

# Initialize Pygame
screen = pygame.display.set_mode((900, 600))

# draft a single character
def draft_character(screen, callback):
    pygame.init()
    traits = []
    click_loop = clickable_lists(pygame.font.SysFont("comic sans", 18), 300, 150, 200, 50)
    textbox = text_box(300, 50, 300, 50, True, "Pick your adventurer!")
    adventurers_draft_list = []
    for i in range(3):
        new_adventurer = character()
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

def draft_party(game_state):
    batch = []
    textbox = text_box(300, 50, 50, 50, True, "Name Your Party")
    write = text_box(300, 150, 50, 50, False)
    batch.append(textbox)
    batch.append(write)
    name = run_screen(screen, batch, [textbox, write], lambda text: setattr(sys.modules[__name__], 'name', text))
    
    new_party = []
    for i in range(4):
        draft_character(screen, lambda adventurer: new_party.append(adventurer))
    party_array = numpy.array(new_party)
    new_party = GuildManager(game_state)
    new_party.guild_members(party_array, name)
    return party(name, new_party, None, 1, 0), party_array

def run_screen(screen, batch, loops, callback):
    pygame.init()
    running = True
    controller = update_display(screen)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        controller.batch_update(batch)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  # Ensure the program exits completely
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for loop in loops:
                    choice = loop.handle_event(event)
                    if choice:
                        callback(choice)
                        running = False
                        # Do not set running to False here to keep the screen on
            elif event.type == pygame.KEYDOWN:
                for loop in loops:
                    loop.handle_event(event)
                    if event.key == pygame.K_RETURN:
                        try:
                            callback(loop.text)
                            running = False
                            return loop.text
                        except Exception:
                            continue  # Continue running the loop if an error occurs

    return  # Ensure the program exits completely

draft_party(None)
