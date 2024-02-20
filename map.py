from random import choice
from typing import Any
from tile import Tile

class Map:
    def __init__(self,size, game):
        self.size = size
        self.game = game
        self.map = [[Tile((x, y), self) for x in range(size[0])] for y in range(size[1])]
    
    def tile(self, pos):
        x, y = pos
        if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
            return None
        return self.map[y][x]
    
    def tiles(self):
        return [tile for row in self.map for tile in row]
    
    def tick(self):
        for row in self.map:
            for tile in row:
                tile.tick()

    def highlight(self, tiles, color = "red"):
        for row in self.map:
            for t in row:
                if t in tiles:
                    print(f"\033[1;31m{t.short()}\033[0m", end=" ")
                else:
                    print(t.short(), end=" ")
            print()
    
    def __str__(self):
        return "Map:\n" + "\n".join(" ".join(tile.short() for tile in row) for row in self.map)
    