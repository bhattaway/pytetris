import pygame

class Grid:
    def __init__(self, w=10, h=20):
        self.w = w
        self.h = h

        self.grid = []

        for i in range(h):
            self.grid.append([None for _ in range(w)])

    def add_tile(self, t, row, col):
        self.grid[row][col] = t

    def add_block(self, b, row, col):
        for t in b.tiles:
            #if b.blocktype
            self.add_tile(t)




    def draw(self, surface):
        pygame.draw.rect(surface, (100,100,100), pygame.Rect(100,40,40*10, 40*20))

        for row in self.grid:
            for t in row:
                if not t is None:
                    t.draw(surface)
        

    def __str__(self):
        s = ""

        for row in self.grid:
            for char in row:
                s += char

            s += '\n'

        return s

    '''
    def __repr__(self):
        s = "   "

        for i in range(self.w):
            s += "%2d" % (i)

        s += '\n'
        i = 0
        for row in self.grid:
            s += "%3d" % (i)
            i += 1
            for char in row:
                s += ' ' + char

            s += '\n'

        return s
    '''
