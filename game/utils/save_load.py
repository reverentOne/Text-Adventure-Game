import pickle, os, sys

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
        'party_list': [],
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