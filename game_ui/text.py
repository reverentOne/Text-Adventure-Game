import pygame
pygame.init()
pygame.font.init()

class text_box():
    def __init__(self, x, y, width, height, locked, text='', wrap=False, font = pygame.font.SysFont("comic sans", 35)):
        self.font = font
        self.x = x
        self.y = y
        self.initial_width = width
        self.initial_height = height
        self.width = width
        self.height = height
        self.text = text
        self.locked = locked
        self.wrap = wrap

    def draw(self, screen):
        # Split the text into lines
        words = self.text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            text_width, _ = self.font.size(test_line)
            if self.wrap:
                if text_width <= self.width - 20:  # 20 is the padding
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + ' '
            else:
                current_line = test_line
                self.width = max(self.initial_width, text_width + 20)  # Update width based on text width
        lines.append(current_line)

        # Update the textbox height based on the number of lines
        padding = 10
        line_height = self.font.get_linesize()
        self.height = max(self.initial_height, len(lines) * line_height + 2 * padding)

        # Draw the textbox
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)

        # Blit the text onto the screen inside the textbox
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, (255, 255, 255))  # White text
            screen.blit(text_surface, (self.x + padding, self.y + padding + i * line_height))

    def handle_event(self, event):
        if not self.locked:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
