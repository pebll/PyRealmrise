from city import City
from termcolor import colored
from random import choice
from constants import TILE_TYPES
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
    
    def available_resources(self):
        return [resource for resource in self.resources if resource.available()]

    def tick(self):
        for res in self.resources:
            if not res.available():
                res.cooldown -= 1
    
    def harvest(self, type):
        available = self.available_resources()
        lg.info(f"Available ressources: {[str(res) for res in available]} Looking for: {type}")

        resource = self.get_resource(type)

        if resource:
            resource.harvest()
            lg.info(f"Harvested {resource} from {self.x}, {self.y}")
            return True
        
        lg.error("Ressource not available")
        return False
    
    def get_resource(self, type):
        resources = [res for res in self.available_resources() if res.resource.name == type.name]
        lg.info(f"Found resources: {[str(res) for res in resources]}")
        if resources:
            return resources[0]
        return None
    
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
        return f"Tile: {self.type.name} at ({self.x}, {self.y}) with {sum([[str(res)] for res in self.resources], [])}"
    
