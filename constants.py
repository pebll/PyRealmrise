from resources import Resource



## Resources

names = ["GRASS", "WATER", "STONE", "WOOD", "SNOW", "SAND"]
RESSOURCES = [Resource(name) for name in names]

res_dict = {str(res): res for res in RESSOURCES}

## Tile Types

class TileType:
    def __init__(self, name, resources):
        self.name = name
        self.short = name[0] + name[1].lower()
        self.resources = resources
    
    def __str__(self):
        return self.short

TILE_TYPES =   [TileType("PLAINS", [res_dict["GRASS"], res_dict["GRASS"]]),
                TileType("FOREST", [res_dict["WOOD"], res_dict["WOOD"]]),
                TileType("MOUNTAIN", [res_dict["STONE"], res_dict["STONE"]]),
                TileType("DESERT", [res_dict["SAND"], res_dict["SAND"]]),
                TileType("SNOWLANDS", [res_dict["SNOW"], res_dict["SNOW"]]),
                TileType("TUNDRA", [res_dict["SNOW"], res_dict["GRASS"]]),
                TileType("OCEAN", [res_dict["WATER"], res_dict["WATER"]]),
                TileType("HILLS", [res_dict["GRASS"], res_dict["STONE"]]),
                TileType("SWAMP", [res_dict["GRASS"], res_dict["WATER"]]),
                TileType("JUNGLE", [res_dict["WOOD"], res_dict["WATER"]]),
                TileType("ICE", [res_dict["SNOW"], res_dict["WATER"]]),
                TileType("BEACH", [res_dict["SAND"], res_dict["WATER"]]),             
                TileType("WETLAND", [res_dict["GRASS"], res_dict["SAND"]]),
                TileType("CANYON", [res_dict["STONE"], res_dict["SAND"]]),
                TileType("GROVE", [res_dict["WOOD"], res_dict["GRASS"]]),
                TileType("SAVANNA", [res_dict["WOOD"], res_dict["SAND"]]),
                TileType("GLACIER", [res_dict["SNOW"], res_dict["STONE"]]),
                TileType("FJORD", [res_dict["WATER"], res_dict["STONE"]]),
                ]

                
              
