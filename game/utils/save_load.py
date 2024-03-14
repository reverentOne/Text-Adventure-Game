import json
import os, sys

def save_game(game_state):
    with open('../assets/data/game_state.json', 'w') as f:
        json.dump(game_state, f)

def load_game():
    if os.path.exists('../assets/data/game_state.json'):
        with open('../assets/data/game_state.json', 'r') as f:
            game_state = json.load(f)
    else:
        game_state = create_initial_game_state()
    return game_state

def create_initial_game_state():
    # Define the initial game state here
    return {
        'player': {
            'name': 'Player 1',
            'health': 100,
            'inventory': []
        },
        'location': 'home'
    }

def exit_game(save_state):
    """Saves game using pickle, then exits."""

    save_game(save_state)
    sys.exit()

def restart_game(*args):
    """Restart game."""

    print("< Restarting Game... >")
    os.execl(sys.executable, sys.executable, *sys.argv)
