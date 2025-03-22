import pygame

class clickable_lists():
    def __init__(self, font, x, y, width, height):
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = []
        self.offset = 0

    def add_option(self, option):
        self.options.append(option)

    def draw(self, screen):
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            w, h = text.get_size()
            screen.blit(text, (self.x + 5, self.y + 5 + (i * 20) - self.offset))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, h*(len(self.options))), 2)

    def handle_event(self, event):
        if event is None:
            return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.offset = max(self.offset - 20, 0)
            elif event.button == 5:  # Scroll down
                self.offset += 20
            elif event.button == 1:  # Left click
                pos = pygame.mouse.get_pos()
                if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
                    index = (pos[1] - self.y + self.offset) // 20
                    if 0 <= index < len(self.options):
                        return self.options[index]

