
#this is the superclass that all game object classes will inherit from
class Gameobject:
    def __init__(self, x, y, w, h, r, g, b, alive=True):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (r, g, b)
        self.alive = alive

    def __init__(self, x, y, w, h, color, alive=True):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.alive = alive

    def __init__(self, rect, color, alive=True):
        self.rect = rect
        self.color = color
        self.alive = alive

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)

    def __str__(self):
        return "<Gameobject rect:%s color:%s alive:%s>" % \
                (self.rect, self.color, self.alive)

