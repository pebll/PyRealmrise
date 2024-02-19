from city import City
from resources import Resource

class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
        self.map = map
        self.resources = {resource: 0 for resource in Resource}
    
    def found_city(self, pos):
        city = City(self.map, pos, self)
        self.cities.append(city)
    
    def get_harvestable_resources(self):
        return sum([city.get_harvestable_resources() for city in self.cities], [])
            
    
    def harvest(self, tile, resource):
        self.resources[resource] += 1


        