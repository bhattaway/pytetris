import pygame
import gameobject

class Tile(gameobject.Gameobject):
    def __init__(self, x, y, w, h, r, g, b, alive):
        super().__init__(alive)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (r,g,b)

    def __str__(self):
        return "<Tile rect:%s color:%s go:%s>" % (self.rect, self.color, super().__str__())

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
