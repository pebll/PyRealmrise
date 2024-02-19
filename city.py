class City:
    def __init__(self, map, pos, realm): 
        self.name = "City"
        self.population = 1
        self.realm = realm
        self.map = map
        self.found(pos)


    def found(self, pos):
        self.tile = self.map.tile(pos)
        self.map.tile(pos).set_building(self)
        x, y = pos
        self.tiles = [self.map.tile((x+1,y)), self.map.tile((x, y+1))]
        for tile in self.tiles:
            tile.set_realm(self.realm)
        self.tile.set_realm(self.realm)

    def get_harvestable_resources(self):
        return sum([[(tile, res) for res in tile.available_resources()] for tile in self.tiles], [])

    def acquire_tile(self, tile):
        self.tiles.append(tile)
        tile.set_realm(self.realm)
        
    def __str__(self):
        return f'{self.name}: {self.population}'