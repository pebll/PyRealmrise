from map import Map
from realm import Realm
from agent import Agent, TestAgent
import logging as lg
from utility import str_list, str_dict


class Game():
    def __init__(self):
        self.map = Map(3, 3)
        self.realm = Realm(self.map)
        self.realm.found_city((1,1))
        self.agent = TestAgent(self.realm)
        self.logger = lg.getLogger("game")
    
    def tick_game(self):
        self.map.tick()
    
    def tick_agent(self, agent):
        actions = agent.choose_actions()
        self.logger.info(f"Agent chose actions: {str_list([action.name for action, _ in actions])}")
        for action, kwargs in actions:
            self.logger.info(f"Activating [{action.name}] with {str_dict(kwargs)}")
            action.activate(**kwargs)
        
    def loop(self):
        for city in self.realm.cities:
            city.tick()
        self.tick_agent(self.agent)
        self.tick_game()

    def start(self):
        self.logger.info("Starting game")
        self.logger.info(self.realm.info())
        self.logger.info(self.map)
        self.logger.info("-"*50)
        for i in range(50):
            self.logger.info(f"Turn {i+1}:")
            self.loop()
            self.logger.info(self.realm.info())
            self.logger.info("-"*50)
        self.logger.info(f"City Tiles: {[str(tile) for tile in self.realm.cities[0].tiles]}")
        self.logger.info(self.map)
        self.logger.info("Game ended")
        