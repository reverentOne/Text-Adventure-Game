with open('saved_games/game_state.json', 'w') as f:
    json.dump(game_state, f)

with open('saved_games/game_state.json', 'r') as f:
    game_state = json.load(f)

import os

if os.path.exists('saved_games/game_state.json'):
    with open('saved_games/game_state.json', 'r') as f:
        game_state = json.load(f)
else:
    game_state = create_initial_game_state()  # You would need to define this function
