import tile
import gameobject

class Block(gameobject.Gameobject):
    def __init__(self, blocktype, dx=0, dy=0, alive=True):
        super().__init__(dx, dy, alive)
        self.blocktype = blocktype
        self.tiles = []
        self.make_tiles()

    def make_tiles(self):
        if self.blocktype == 'o':
            red=255
            green=255
            blue=0
            self.tiles.append(tile.Tile(x=0, y=0, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=50, y=0, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=50, y=50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=0, y=50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 'i':
            red=150
            green=150
            blue=255
            self.tiles.append(tile.Tile(x=0, y=0, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=0, y=50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=0, y=100, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=0, y=150, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)
