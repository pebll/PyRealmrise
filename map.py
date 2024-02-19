from random import choice
from tile_types import TileTypes

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
        return "\n".join(" ".join(str(tile) for tile in row) for row in self.map)
    



class Tile:
    def __init__(self, x, y, random=True):
        self.x = x
        self.y = y
        self.type = choice(list(TileTypes))
        self.resources = self.type.value.resources
        self.cooldowns = [0 for _ in self.resources]
        self.realm = None
    
    def available_resources(self):
        return [ressource for ressource, cooldown in zip(self.resources, self.cooldowns) if cooldown == 0]

    def tick(self):
        for i in range(len(self.cooldowns)):
            if self.cooldowns[i] > 0:
                self.cooldowns[i] -= 1
    
    def harvest(self, ressource):
        index = self.resources.index(ressource)
        if self.cooldowns[index] == 0:
            self.cooldowns[index] = 3
            return 1
        print(KeyError("Ressource not available"))
        return 0
    
    def set_building(self, building):
        self.building = building
    
    def set_realm(self, realm):
        self.realm = realm

    def __str__(self):
        return f"( {self.type} )"
    
