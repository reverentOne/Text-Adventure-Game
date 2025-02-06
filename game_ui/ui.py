import pygame
class set_up_background():
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw(self):
        self.screen.fill((0, 0, 0))

class update_display():
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    
    def batch_update(self, list, rects=None):
        self.screen.fill((0, 0, 0))
        for item in list:
            item.draw(self.screen)
        if rects:
            pygame.display.update(rects)
        else:
            pygame.display.flip()