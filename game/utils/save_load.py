import json
import os

def save_game(game_state):
    with open('../assets/data/game_state.json', 'w') as f:
        json.dump(game_state, f)

def load_game():
    if os.path.exists('../assets/data/game_state.json'):
        with open('../assets/data/game_state.json', 'r') as f:
            game_state = json.load(f)
    else:
        game_state = create_initial_game_state()  # You would need to define this function
    return game_state
