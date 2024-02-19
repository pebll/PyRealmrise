from city import City
from resources import Resource

class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
        self.map = map
        self.resources = {resource: 0 for resource in Resource.__members__.values()}
    
    def found_city(self, pos):
        city = City(self.map, pos, self)
        self.cities.append(city)
    
    def get_harvestable_resources(self):
        return sum([city.get_harvestable_resources() for city in self.cities], [])
            
    
    def harvest(self, tile, resource):
        if tile.harvest(resource):
            self.resources[resource] += 1
        
    def info(self):
        info = ""
        info += f"Realm: {self.name}\n"
        info += f"Resources: {[f'{res} : {count}' for (res, count) in self.resources.items()]}\n"
        info += f"Cities: {[str(city) for city in self.cities]}\n"
        info += f"Harvestable resources: {sum([[str(res[1])] for res in self.get_harvestable_resources()], [])}\n"
        return info
    
        