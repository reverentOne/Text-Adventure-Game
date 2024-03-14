import sys, os
from game.utils import save_load

def show_title():
    """Show game title, tips, and player stats."""

    show_art('start banner')
    print(f"""
    ---------- Text Adventure Game ----------
    {game_art1}
    \nHere are some basic commands to get you started: 
        /help: Opens the help menu
        /settings: Opens the game settings menu
        /exit: Save your progress and exit the game
        \nRemember, this is your adventure. Make the most of it!\n
    -----------------------------------------------------\n""")

def show_game_over():
    """Show game over message and stats."""

    show_art('game over')
    print(f"""
    ---------- Game Over ----------
    {game_art2}
    \nThank you for playing!\n\nPlay again?
    """)
    if str(input('No / Yes or Enter > ')).lower() in ['n', 'no']: save_load.exit_game(create_initial_game_state())
    else: save_load.restart_game()
    sys.exit()


def show_hud():
    # Code to display the HUD (Heads-Up Display)

def show_settings():
    # Code to display the game settings

def show_version(game_version, version_date):
    """Shows game version."""

    print(f"\n    Version: {game_version} ({version_date})")
    sys.exit()

def show_help():
    print("""\n        -------------------- HELP -------------------- 
    
    Commands:
        inv                     -- Show inventory.
        stats TARGET            -- Show states of a character, item, or enemy. E.g. 'stats John Doe', 'stats short sword'
        /help                   -- Show this help page.
        /settings               -- Shows or change game settings. E.g. '/settings', '/settings hud off', '/settings hardcore on'
        /reset                  -- Deletes current save and restarts game.
        /save                   -- Saves the game.
        /exit                   -- Saves and Exits the game.
        """)

def show_sysargs():
    """Shows available runtime arguments."""

    print("""
    --help      --  This help page.
    --version   --  Show version.
    --nocrawl   --  Disable text crawl effect.
    --noart     --  Diable ASCII art.
    --nohud     --  Disable game HUD.
    --nohints   --  Disable game hints.
    --hardcore  --  Enable Hardcore mode.
    --fastmode  --  Enable Fast mode, goes through storyline actions as quick as possible. Also disables text crawl and ascii art.""")
    sys.exit()
