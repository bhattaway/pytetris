import pygame
import gameobject

class Tile(gameobject.Gameobject):
    def __init__(self, x, y, w, h, r, g, b, dx=0, dy=0, alive=True):
        super().__init__(dx, dy, alive)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (r,g,b)

    def __str__(self):
        return "<Tile %s color:%s %s>" % (self.rect, self.color, super().__str__())

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
