import logging as lg
from logging_config import configure_logging

class Agent:
    def __init__(self, realm):
        self.realm = realm
        self.logger = lg.getLogger("agent")
        configure_logging("agent")

    def choose_harvests(self):
        return None

    def choose_actions(self):
        actions = [] # list of all actions the agent wants to take in the form of (action, kwargs)
        self.choose_harvests()
        return actions

class TestAgent(Agent):
    def choose_harvests(self):
        for city in self.realm.cities:
            left_tiles = city.tiles
            harvests = []
            for _ in range(city.population):
                while left_tiles:
                    tile = left_tiles.pop()
                    resources = tile.available_resources()
                    if resources:
                        harvests.append(resources[0])
                        break
            if harvests:
                self.actions.append((city.harvest_action, {"harvests": harvests}))