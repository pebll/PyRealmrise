from enum import Enum

class Resource(Enum):
    GRASS = 0
    WATER = 1
    STONE = 2
    WOOD = 3
    SNOW = 4
    SAND = 5

    def __str__(self):
        return self.name