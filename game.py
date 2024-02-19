from map import Map
from realm import Realm
from agent import Agent, TestAgent
import logging as lg

class Game():
    def __init__(self):
        self.map = Map(3, 3)
        self.realm = Realm(self.map)
        self.realm.found_city((1,1))
        self.agent = TestAgent(self.realm)
    
    def tick_game(self):
        self.map.tick()
    
    def tick_agent(self, agent):
        actions = agent.choose_actions()
        self.apply_actions(self.realm, actions)

    def apply_actions(self, realm, actions):
        for action, targets in actions.items():
            if targets:
                if action == "harvests":
                    for target in targets:
                        realm.harvest(target)
    
    def loop(self):
        self.tick_agent(self.agent)
        self.tick_game()

    def start(self):
        lg.basicConfig(level=lg.INFO)
        lg.info("Starting game")
        lg.info(self.realm.info())
        lg.info(self.map)
        lg.info("-"*50)
        for i in range(10):
            lg.info(f"Turn {i+1}:")
            self.loop()
            lg.info(self.realm.info())
            lg.info("-"*50)
        lg.info(f"City Tiles: {[str(tile) for tile in self.realm.cities[0].tiles]}")
        lg.info(self.map)
        lg.info("Game ended")
        