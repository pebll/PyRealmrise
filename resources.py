

class Resource():
    def __init__(self, name):
        self.name = name
        self.cooldown = 5

    def __str__(self):
        return self.name
    
class TileResource():
    def __init__(self, resource, tile):
        self.resource = resource
        self.name = resource.name
        self.cooldown = 0
        self.tile = tile
    
    def available(self):
        return self.cooldown == 0
    
    def harvest(self):
        self.cooldown = self.resource.cooldown

    def __str__(self):
        return f"{self.resource} ({self.cooldown})"