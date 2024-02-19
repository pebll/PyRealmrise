from city import City
from resources import Resource
class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
        self.resources = {resource: 0 for resource in Resource}
    
    def found_city(self, pos):
        city = City(self.map, pos)
        self.cities.append(city)


        