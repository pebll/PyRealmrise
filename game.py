from map import Map
from realm import Realm
from agent import Agent, TestAgent

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
                        tile, resource = target
                        realm.harvest(tile, resource)
    
    def loop(self):
        self.tick_agent(self.agent)
        self.tick_game()

    def start(self):
        print("Starting game")
        print(self.realm.info())
        print(self.map)
        print("-"*50)
        for i in range(10):
            print(f"Turn {i+1}:")
            self.loop()
            print(self.realm.info())
            print("-"*50)
        print(f"City Tiles: {[str(tile) for tile in self.realm.cities[0].tiles]}")
        print(self.map)
        print("Game ended")
        