
import pygame
import sys
from ui import update_display

def run_screen(screen, batch, loops=None, callback=None):
    pygame.init()
    running = True
    controller = update_display(screen)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        controller.batch_update(batch)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  # Ensure the program exits completely
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if loops is not None:
                    for loop in loops:
                        choice = loop.handle_event(event)
                        if choice:
                            callback(choice)
                            running = False
            elif event.type == pygame.KEYDOWN:
                if loops is not None:
                    for loop in loops:
                        if loop.locked == False:
                            loop.handle_event(event)
                            if event.key == pygame.K_RETURN:
                                try:
                                    callback(loop.text)
                                    running = False
                                    return loop.text
                                except Exception:
                                    continue  

    return  # Ensure the program exits completely