import pygame
pygame.init()
pygame.font.init()
class text_box():
    def __init__(self, x, y, width, height, text=''):
        self.font = pygame.font.SysFont("comic sans", 35)
        self.x = x
        self.y = y
        self.initial_width = width
        self.initial_height = height
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        # Render the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # White text
        text_width, text_height = text_surface.get_size()
        
        # Update the textbox size based on text size with padding
        padding = 10
        self.width = max(self.initial_width, text_width + 2 * padding)
        self.height = max(self.initial_height, text_height + 2 * padding)
        
        # Draw the textbox
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        
        # Blit the text onto the screen inside the textbox
        screen.blit(text_surface, (self.x + padding, self.y + (self.height - text_height) // 2))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
