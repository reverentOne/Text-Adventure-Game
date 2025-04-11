import sys
import pathlib
# Get the root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
import pygame
from screen_manager import run_screen
from text import text_box
from buttons import clickable_lists
from game.drafting_party import draft_party
from game.utils.guild_manager import GuildManager

screen = pygame.display.set_mode((900, 600))

def start_screen(screen, gamestate):
    font = pygame.font.SysFont("Arial", 24)
    choice = clickable_lists(font, 50, 50, 200, 50)  # Create clickable list
    manage = GuildManager(gamestate)

    options = [
        "Draft Party",  # Add a second element to each tuple
        "Manage Guild"  # Add a second element to each tuple
    ]

    for option in options:
        choice.add_option(option)

    # Render the screen and get the selected option
    batch = [choice]
    selected_option = run_screen(screen, batch, [choice], lambda choice: choice)
    print(selected_option)
    # Execute the corresponding action
    return selected_option

start_screen(screen, 1)