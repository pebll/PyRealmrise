from map import Map
from realm import Realm
from agent import Agent, TestAgent
import logging as lg
from utility import str_list, str_dict
import random


class Game():
    def __init__(self, mapsize = (5,5), starting_resources = 3, turns = 10, agent = TestAgent, seed = None):
        if not seed:
            self.seed = random.randint(0, 1000000)
        else:
            self.seed = seed
        self.rng = random.Random(self.seed)
        self.map = Map(mapsize, self)
        self.max_turns = turns
        self.realm = Realm(self.map)
        self.realm.found_city((mapsize[0]//2, mapsize[1]//2))
        self.agent = agent(self.realm)
        self.logger = lg.getLogger("game")
        self.city = self.realm.cities[0]
        for res in self.realm.resources:
            self.realm.resources[res] = starting_resources
     
    
    def tick_game(self):
        self.map.tick()
    
    def tick_agent(self, agent):
        actions = agent.choose_actions()
        for action, kwargs in actions:
            action.activate(**kwargs)
        
    def loop(self):
        self.realm.tick()
        self.tick_agent(self.agent)
        self.tick_game()

    def start(self):
        for _ in range(self.max_turns):
            self.loop()

class TestGame(Game):
    def __init__(self, mapsize=(5, 5), starting_resources=3, turns=10, agent=TestAgent, seed=None):
        super().__init__(mapsize, starting_resources, turns, agent, seed)
        history_keys = ["resource_count", "total_population", "total_tiles", "score"]
        self.history = {key: [] for key in history_keys}

    def loop(self):
        self.add_history()
        return super().loop()

    def start(self):
        super().start()
        self.add_history()

    def add_history(self):
        stats = self.realm.get_stats()
        for key in stats.keys():
            self.history[key].append(stats[key])
    


class LogGame(Game):
    def start(self):
        self.logger.info("Starting game")
        self.logger.info(self.realm.info())
        self.logger.info(self.map)
        self.logger.info("-"*50)
        for i in range(self.max_turns):
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
    
    def tick_agent(self, agent):
        actions = agent.choose_actions()
        self.logger.info(f"Agent's turn with actions: {str_list([action.name for action, _ in actions])}")
        for action, kwargs in actions:
            action.activate(**kwargs)
            self.logger.info(f"Agent activated {action.name} with {str_dict(kwargs)}")

    

        