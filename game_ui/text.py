import pygame

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

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Welcome")
clock = pygame.time.Clock()
textbox = text_box( 50, 50, 200, 50, "Type here")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        textbox.handle_event(event)  # Pass events to the textbox

    screen.fill((0, 0, 0))  # Clear the screen
    textbox.draw(screen)  # Draw the textbox
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()