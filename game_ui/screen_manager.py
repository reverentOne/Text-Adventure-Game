import sys
import pathlib
# Get the root directory of the project
root_dir = pathlib.Path(__file__).resolve().parent.parent
# Add the root directory to sys.path
sys.path.append(str(root_dir))
import pygame
from game_ui.ui import update_display

def run_screen(screen, batch, interactables, callback):
    pygame.init()
    running = True
    controller = update_display(screen)
    selected_option = None  # Initialize selected option
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        controller.batch_update(batch)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  # Ensure the program exits completely
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for interactable in interactables:
                    result = interactable.handle_event(event)
                    if result is not None:
                        selected_option = callback(result)
                        running = False
                            
            elif event.type == pygame.KEYDOWN:
                for interactable in interactables:
                    try:
                        if interactable.locked == False:
                            interactable.handle_event(event)
                            if event.key == pygame.K_RETURN:
                                try:
                                    selected_option = callback(interactable.text)
                                    running = False
                                    return interactable.text
                                except Exception:
                                    continue  
                    except Exception:
                        continue
                        
    return selected_option  # Return the selected option