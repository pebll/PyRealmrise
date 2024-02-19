from city import City
from termcolor import colored
from random import choice
from constants import TILE_TYPES, RESSOURCES
from resources import TileResource
import logging as lg

class Tile:
    def __init__(self, x, y, type=None):
        self.lg = lg.getLogger(f"Tile({x},{y})")
        self.x = x
        self.y = y

        self.type = type if type else choice(TILE_TYPES)

        self.resources = self.type.resources
        self.resources = [TileResource(res, self) for res in self.resources]
        self.realm = None
        self.building = None

        self.base_cost = [choice(RESSOURCES) for _ in range(10)]
        self.special_cost = [choice(self.type.resources) for _ in range(10)]
    
    def get_cost(self, distance):
        return self.base_cost[:distance-1] + self.special_cost[:1+distance//3]

    def available_resources(self):
        return [resource for resource in self.resources if resource.available()]

    def tick(self):
        for res in self.resources:
            if not res.available():
                res.cooldown -= 1
    
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
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
        return f"{self.type.name} at ({self.x}, {self.y}) with {sum([[str(res)] for res in self.resources], [])}"
    
