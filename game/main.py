import pathlib, sys, os
from ui import display
import drafting_party
from combat import combat
#from game_files.output import show_title, show_help, show_version  # Customize these
#from game_files.player import Player  # Assuming you have a Player class

# Metadata
__version__ = "0.1.0"  # Start with an early version
__date__ = '2023-08-17'  # Today's date
__author__ = "Your Name"
__email__ = "your_email@example.com"  # Replace with your information

# --- Main Execution ---
if __name__ == '__main__':
    if '--help' in sys.argv:
        display.show_help()
    if '--version' in sys.argv:
        display.show_version(__version__, __date__)

    # Start the game
    display.show_title()
    while True:
        combat.combat()
        break
        # ... game logic will go here ...