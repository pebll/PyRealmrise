from map import Map
from realm import Realm
from agent import Agent, TestAgent
import logging as lg
from utility import str_list, str_dict


class Game():
    def __init__(self):
        self.map = Map(5, 5)
        self.realm = Realm(self.map)
        self.realm.found_city((2,2))
        self.agent = TestAgent(self.realm)
        self.logger = lg.getLogger("game")
        self.city = self.realm.cities[0]
        for res in self.realm.resources:
            self.realm.resources[res] = 3
     
    
    def tick_game(self):
        self.map.tick()
    
    def tick_agent(self, agent):
        actions = agent.choose_actions()
        self.logger.info(f"Agent chose actions: {str_list([action.name for action, _ in actions])}")
        for action, kwargs in actions:
            self.logger.info(f"Activating [{action.name}] with {str_dict(kwargs)}")
            action.activate(**kwargs)
        
    def loop(self):
        self.realm.tick()
        self.tick_agent(self.agent)
        self.tick_game()

    def start(self):
        self.logger.info("Starting game")
        self.logger.info(self.realm.info())
        self.logger.info(self.map)
        self.logger.info("-"*50)
        for i in range(10):
            self.logger.info(f"Turn {i+1}:")
            self.loop()
            self.logger.info(self.realm.info())
            self.logger.info("-"*50)
        self.logger.info(f"City Tiles: {[str(tile) for tile in self.city.tiles]}")
        self.logger.info(self.map)
        self.logger.info(f"Acquirable tiles:")
        for tile in self.realm.cities[0].acquirable_tiles():
            self.logger.debug(f"Tile {tile} costs: {str_list(tile.get_cost(tile.distance(self.city.tile)))}")
        self.logger.info("Next population increase costs:")
        for cost in self.city.pop_costs[self.city.population-1:self.city.population+2]:
            self.logger.debug(f"{str_list(cost)}")
        self.logger.info("Game ended")
    

        