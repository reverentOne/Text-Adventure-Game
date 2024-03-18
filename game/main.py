import pathlib, sys, os
#Get root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))


from ui import display
from drafting_party import draft_party
from chapters import chapter1, chapter2

# Metadata
__version__ = "0.1.0"
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
    party = draft_party()
    party = chapter1(party)
    chapter2(party)