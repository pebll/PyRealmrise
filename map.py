from random import choice
from typing import Any
from tile import Tile

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[Tile(x, y) for x in range(width)] for y in range(height)]
    
    def tile(self, pos):
        x, y = pos
        return self.map[x][y]
    
    def tick(self):
        for row in self.map:
            for tile in row:
                tile.tick()
    
    def __str__(self):
        return "\n".join(" ".join(tile.short() for tile in row) for row in self.map)
    