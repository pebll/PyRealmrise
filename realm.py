from city import City

class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
    
    def found_city(self, pos):
        city = City(self.map, pos)
        self.cities.append(city)

    
        