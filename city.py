

class City:
    def __init__(self, map, pos, realm): 
        self.name = "City"
        self.population = 1
        self.realm = realm
        self.map = map
        self.found(pos)


    def found(self, pos):
        self.pos = pos
        self.map.tile(pos).set_building(self)
        x, y = pos
        self.tiles = [(x+1,y), (x, y+1)]
        for tile in self.tiles:
            self.map.tile(tile).set_realm(self.realm)

    def get_harvestable_resources(self):
        return sum([self.map.tile(tile).available_resources() for tile in self.tiles], [])


    def __str__(self):
        return f'{self.name}: {self.population}'