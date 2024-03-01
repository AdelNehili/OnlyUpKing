import pygame

class Platform:
    def __init__(self, pos, size):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.size = pygame.Vector2(size[0], size[1])
        self.color = (0, 255, 0) #GREEN

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.rect(screen, self.color, (self.pos.x + offset_x, self.pos.y + offset_y, self.size.x, self.size.y))
