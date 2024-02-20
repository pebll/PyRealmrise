from random import choice
from typing import Any
from tile import Tile

class Map:
    def __init__(self,size):
        self.size = size
        self.map = [[Tile(x, y) for x in range(size[0])] for y in range(size[1])]
    
    def tile(self, pos):
        x, y = pos
        if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
            return None
        return self.map[x][y]
    
    def tiles(self):
        return [tile for row in self.map for tile in row]
    
    def tick(self):
        for row in self.map:
            for tile in row:
                tile.tick()
    
    def __str__(self):
        return "Map:\n" + "\n".join(" ".join(tile.short() for tile in row) for row in self.map)
    