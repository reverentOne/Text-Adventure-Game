import pickle, os, sys, numpy
import sys
import pathlib

# Add the root directory to sys.path
root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

def save_game(game_state):
    with open('assets/data/game_state.pkl', 'wb') as f:
        pickle.dump(game_state, f)

def load_game():
    if os.path.exists('assets/data/game_state.pkl'):
        with open('assets/data/game_state.pkl', 'rb') as f:
            game_state = pickle.load(f)
    else:
        game_state = create_initial_game_state()
    return game_state
def create_initial_game_state():
    # Define the initial game state here
    return {
        'guild_teams' : [],
        'location': {
            'name': "",
            'description': "",
            'items': [],
            'enemies': []
        },
        'game_progress': {
            'floor': 0,
            'chapter': 0,
            'quests_completed': [],
            'bosses_defeated': 0
        },
        'settings': {
            'textcrawl': True,
            'hud': True,
            'difficulty': 'normal',
            'art/ascii': True
        },
        'loot': {
            'gold': 0,
            'inventory': numpy.zeros((5, 5), dtype=object),
            'common experience': 0,
            'uncommon experience': 0,
            'rare experience': 0,
            'epic experience': 0,
            'legendary experience': 0,
            'common shards': 0,
            'uncommon shards': 0,
            'rare shards': 0,
            'epic shards': 0,
            'legendary shards': 0
        }
    }
def exit_game(save_state):
    """Saves game using pickle, then exits."""
    save_game(save_state)
    sys.exit()

def restart_game(*args):
    """Restart game."""
    print("< Restarting Game... >")
    os.execl(sys.executable, sys.executable, *sys.argv)