import logging as lg
from logging_config import configure_logging
from utility import str_list, to_dict_resources

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

class UtilityAgent(Agent):
    def possible_actions(self):
        actions = []
        for city in self.realm.cities:
            for action in city.actions.values():
                actions.append(action)
        return actions
