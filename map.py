from random import choice
from typing import Any
from tile_types import TileTypes
from city import City
from termcolor import colored

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
    



class Tile:
    def __init__(self, x, y, random=True):
        self.x = x
        self.y = y
        self.type = choice(list(TileTypes))
        self.resources = self.type.value.resources
        self.resources = [[res, 0] for res in self.resources]
        self.realm = None
        self.building = None
    
    def available_resources(self, with_cool_down=False):
        if with_cool_down:
            return [[ressource, cooldown] for ressource, cooldown in self.resources if cooldown == 0]
        return [ressource for ressource, cooldown in self.resources if cooldown == 0]

    def tick(self):
        for res in self.resources:
            if type(res) == tuple:
                print(self.x, self.y, res)
            if res[1] > 0:
                res[1] -= 1
    
    def harvest(self, ressource):
        available = self.available_resources()
        print("[INFO] Available ressources: ", available, "Looking for: ", ressource)
        try:
            index = self.resources.index([ressource, 0])
            self.resources[index] = [ressource, 3]
            print(f"[INFO] Harvested {ressource} from {self.x}, {self.y}")
            return 1
        except ValueError:
            print("[ERROR] Ressource not available")
            return 0
    
    def set_building(self, building):
        self.building = building
    
    def set_realm(self, realm):
        self.realm = realm

    def short(self):
        short = f"( {self.type} )"
        if type(self.building) == City:
            short = " [C] "
        if self.realm:
            short = colored(short, 'blue', attrs=['bold'])
        return short

    def __str__(self) -> str:
        return f"Tile: {self.type.name} at ({self.x}, {self.y}) with {sum([[f'{str(res[0])} ({res[1]})'] for res in self.resources], [])}"
    
