import pathlib, sys, os
import pygame

#Get root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
from game_ui import ui
import numpy
from ui import display as di
from drafting_party import draft_party
from utils.guild_manager import GuildManager
#from chapters import chapter1, chapter2, chapter1_1
from utils import save_load as sl

# Metadata
__version__ = "0.1.0"
__date__ = '2023-08-17'  # Today's date
__author__ = "Your Name"
__email__ = "your_email@example.com"  # Replace with your information

# --- Main Execution ---
if __name__ == '__main__':
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((900, 600))  # Create a Pygame window
    pygame.display.set_caption("Text Adventure Game")  # Set the window title

    # Load the game state
    gs = sl.load_game()
    # Check if there are any guild teams
    if len(gs["guild_teams"]) == 0:  # Access the 'guild_teams' key from the loaded game state
        draft_party(gs,screen)
    man = GuildManager(gs)
    man.view_guild(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window close event
                running = False
        screen.fill((0,0,0))
        pygame.display.flip()

    pygame.quit() 


