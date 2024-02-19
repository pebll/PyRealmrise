from city import City
from constants import RESSOURCES
import logging as lg
from utility import to_dict_cost


class Realm:
    def __init__(self, map):
        self.name = "Realm"
        self.cities = []
        self.map = map
        self.resources = {str(resource): 0 for resource in RESSOURCES}
        self.logger = lg.getLogger(self.name.lower())
    
    def found_city(self, pos):
        city = City(self.map, pos, self)
        self.cities.append(city)
    
    def get_harvestable_resources(self):
        return sum([city.get_harvestable_resources() for city in self.cities], [])          
    
    def tick(self):
        for city in self.cities:
            city.tick()

    def can_afford(self, cost):
        if cost == None:
            return True
        if type(cost) == list:
            cost = to_dict_cost(cost)
        return all([self.resources[res] >= cost[res] for res in cost])

    def pay(self, cost):
        self.logger.info(f"Paying {cost}, {self.resources}")
        if cost:
            for res in cost:
                self.resources[res] -= cost[res]
            self.logger.info(f"-> {self.resources}")

    def info(self):
        info = ""
        info += f"Realm: {self.name}\n"
        info += f"Resources: {[f'{res} : {count}' for (res, count) in self.resources.items()]}\n"
        info += f"Cities: {[str(city) for city in self.cities]}\n"
        info += f"Harvestable resources: {sum([[str(res)] for res in self.get_harvestable_resources()], [])}"
        return info
    
        