import pathlib, sys, os
#Get root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))


from ui import display as di
from drafting_party import draft_party
from chapters import chapter1, chapter2
from utils import save_load as sl

# Metadata
__version__ = "0.1.0"
__date__ = '2023-08-17'  # Today's date
__author__ = "Your Name"
__email__ = "your_email@example.com"  # Replace with your information

# --- Main Execution ---
if __name__ == '__main__':
    if '--help' in sys.argv:
        di.show_help()
    if '--version' in sys.argv:
        di.show_version(__version__, __date__)

    # Start the game
    di.show_title()
    gs = sl.load_game()
    if len(gs['guild_party_name_matrix'][0]) == 0: draft_party()
    print(gs['guild_party_name_matrix'])
    gs = chapter1.chapter1(gs)
    sl.exit_game(gs)
    