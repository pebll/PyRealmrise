import logging as lg
from logging_config import configure_logging
from utility import str_list

class Agent:
    def __init__(self, realm):
        self.realm = realm
        self.logger = lg.getLogger("agent")
        self.actions = []

    def choose_harvests(self):
        return None

    def choose_actions(self):
        self.actions = [] # list of all actions the agent wants to take in the form of (action, kwargs)
        self.choose_harvests()
        return self.actions

class TestAgent(Agent):

    def choose_pop(self):
        for city in self.realm.cities:
            if self.realm.can_afford(city.increase_pop_cost()):
                self.logger.info(f"Chose to increase population")
                self.actions.append((city.actions["increase_pop"], {}))

    def choose_tile(self):
        for city in self.realm.cities:
            for tile in city.tiles:
                if self.realm.can_afford(tile.get_cost(tile.distance(city.tile))):
                    self.logger.info(f"Chose to acquire tile {tile}")
                    self.actions.append((city.actions["acquire_tile"], {"tile": tile}))
    def choose_actions(self):
        self.actions = []
        self.choose_pop()
        self.choose_tile()
        self.choose_harvests()
        return self.actions
    
    def choose_harvests(self):
        for city in self.realm.cities:
            left_tiles = list(city.tiles)
            harvests = []
            for _ in range(city.population):
                while left_tiles:
                    tile = left_tiles.pop()
                    resources = tile.available_resources()
                    if resources:
                        harvests.append(resources[0])
                        break
            if harvests:
                self.logger.info(f"Chose to harvest {str_list(harvests)}")
                self.actions.append((city.actions["harvest"], {"harvests": harvests}))