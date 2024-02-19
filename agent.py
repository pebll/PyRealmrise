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
        actions = {}
        actions["harvests"] = self.choose_harvests()
        return actions

class TestAgent(Agent):
    def choose_harvests(self):
        harvestables = self.realm.get_harvestable_resources()
        if harvestables:
            self.logger.info(f"Choosing to harvest {harvestables[0].name} from {harvestables[0].tile}")
            return [harvestables[0]]
        return None