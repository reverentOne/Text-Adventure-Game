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

def start_screen(screen, gamestate):
    font = pygame.font.SysFont("Arial", 24)
    choice = clickable_lists(font, 50, 50, 200, 50)  # Create clickable list
    manage = GuildManager(gamestate)

    # Define options and their corresponding actions
    options = [
        ("Draft", lambda: draft_party(gamestate, screen)),  # Draft Party action
        ("Manage Guild", lambda: manage.view_guild(screen))  # Manage Guild action
    ]

    # Add options to the clickable list
    for option, _ in options:
        choice.add_option(option)

    # Render the screen and get the selected option
    batch = [choice]
    selected_option = run_screen(screen, batch, [choice], lambda choice: choice)

    # Execute the corresponding action
    for option, action in options:
        if option == selected_option:
            action()  # Call the action associated with the selected option
            break

class ScreenNode:
    def __init__(self, name, options=None, callback=None):
        self.name = name  # Name of the screen
        self.options = options or []  # List of options (clickable lists or buttons)
        self.callback = callback  # Function to execute when an option is selected
        self.next_screens = {}  # Dictionary mapping options to next screens

    def add_option(self, option_text, next_screen):
        """Add an option and its corresponding next screen."""
        self.options.append(option_text)
        self.next_screens[option_text] = next_screen

def create_screen_tree(screen, game_state):
    # Create the root screen
    root = ScreenNode("Start Screen")

    # Create other screens
    screen1 = ScreenNode("Screen 1")
    screen2 = ScreenNode("Screen 2")
    screen3 = ScreenNode("Screen 3")

    # Add options to the root screen
    root.add_option("Go to Screen 1", screen1)
    root.add_option("Go to Screen 2", screen2)

    # Add options to Screen 1
    screen1.add_option("Go to Screen 3", screen3)
    screen1.add_option("Back to Start", root)

    # Add options to Screen 2
    screen2.add_option("Back to Start", root)

    # Add options to Screen 3
    screen3.add_option("Back to Screen 1", screen1)

    return root

def run_tree(screen, game_state):
    current_screen = create_screen_tree(screen, game_state)  # Start at the root screen
    font = pygame.font.SysFont("Arial", 24)

    while current_screen:
        # Create clickable lists for the current screen's options
        clickable_list = clickable_lists(font, 50, 50, 200, 50)  # x, y, width, height
        for option in current_screen.options:
            clickable_list.add_option(option)

        # Render the current screen
        batch = [clickable_list]
        selected_option = run_screen(screen, batch, [clickable_list], lambda choice: choice)

        # Handle the selected option
        if selected_option in current_screen.next_screens:
            current_screen = current_screen.next_screens[selected_option]
        else:
            current_screen = None  # Exit the tree if no valid option is selected

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Option Tree Example")

game_state = {}  # Example game state
start_screen(screen, game_state)

