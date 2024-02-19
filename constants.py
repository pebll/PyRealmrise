from resources import Resource

## Resources

names = ["GRASS", "WATER", "STONE", "WOOD", "SNOW", "SAND"]
RESSOURCES = [Resource(name) for name in names]

res_dict = {str(res): res for res in RESSOURCES}

## Tile Types

class TileType:
    def __init__(self, name, resources):
        self.name = name
        self.short = name[0]
        self.resources = resources

TILE_TYPES = [TileType("PLAINS", [res_dict["GRASS"], res_dict["GRASS"]]),
                TileType("FOREST", [res_dict["WOOD"], res_dict["WOOD"]]),
                TileType("MOUNTAIN", [res_dict["STONE"], res_dict["STONE"]]),
                TileType("DESERT", [res_dict["SAND"], res_dict["SAND"]]),
                TileType("TUNDRA", [res_dict["SNOW"], res_dict["SNOW"]]),
                TileType("OCEAN", [res_dict["WATER"], res_dict["WATER"]])]
                
              
