from city import City
from constants import RESSOURCES

class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
        self.map = map
        self.resources = {str(resource): 0 for resource in RESSOURCES}
    
    def found_city(self, pos):
        city = City(self.map, pos, self)
        self.cities.append(city)
    
    def get_harvestable_resources(self):
        return sum([city.get_harvestable_resources() for city in self.cities], [])          
        
    def info(self):
        info = ""
        info += f"Realm: {self.name}\n"
        info += f"Resources: {[f'{res} : {count}' for (res, count) in self.resources.items()]}\n"
        info += f"Cities: {[str(city) for city in self.cities]}\n"
        info += f"Harvestable resources: {sum([[str(res)] for res in self.get_harvestable_resources()], [])}"
        return info
    
        