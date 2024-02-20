from action import Harvest, AcquireTile, IncreasePop
import logging as lg
from random import choice
from constants import RESSOURCES
from utility import str_list


class City:
    def __init__(self, map, pos, realm):    
        self.name = "City"
        self.logger = lg.getLogger(self.name.lower())
        self.population = 1
        self.realm = realm
        self.map = map
        self.actions = {}
        self.actions["harvest"] = Harvest(self.realm, self)
        self.actions["acquire_tile"] = AcquireTile(self.realm, self)
        self.actions["increase_pop"] = IncreasePop(self.realm, self)
        self.tiles = []
        self.found(pos)
        self.pop_costs = [[choice(RESSOURCES) for _ in range((i+1)*2)] for i in range(20)]
        

    def found(self, pos):
        self.tile = self.map.tile(pos)
        self.logger.info(f"Founded city at {pos}")
        self.map.tile(pos).set_building(self)
        x, y = pos
        for tile in [self.map.tile((x-1,y)), self.map.tile((x, y-1))]:
            self.acquire_tile(tile)
        self.tile.set_realm(self.realm)

    def tick(self):
        for action in self.actions.values():
            action.tick()

    def get_harvestable_resources(self):
        return sum([[res for res in tile.available_resources()] for tile in self.tiles], [])

    def harvest(self, resource):
        self.realm.resources[resource.name] += 1
        resource.harvest()

    def acquire_tile(self, tile):
        self.tiles.append(tile)
        tile.set_realm(self.realm)
        self.logger.info(f"Acquired tile {tile}")
    
    def acquirable_tiles(self):
        neighbours = set()
        own_tiles = set(self.tiles) | {self.tile}

        for tile in own_tiles:
            potential_neighbours = tile.neighbours()
            for neighbour in set(potential_neighbours):
                if neighbour.realm != self.realm and neighbour not in own_tiles:
                    neighbours.add(neighbour)
        return list(neighbours)
    
    def increase_population(self):
        self.population += 1
        self.logger.info(f"Population increased to {self.population}")
    
    def increase_pop_cost(self):
        return self.pop_costs[self.population-1]
    
    def __str__(self):
        return f'{self.name}: {self.population}'
