from enum import Enum
from resources import Resource

class TileType:
    def __init__(self, name, resources):
        self.name = name
        self.short = name[0]
        self.resources = resources
 
class TileTypes(Enum):
    PLAINS = TileType("Plains", [Resource.GRASS, Resource.WOOD])
    SEA = TileType("Sea", [Resource.WATER, Resource.SAND])
    MOUNTAIN = TileType("Mountain", [Resource.STONE, Resource.STONE])

    def __str__(self):
        return self.value.short