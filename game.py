from map import Map
from realm import Realm

class Game():
    def __init__(self):
        self.map = Map(5, 5)
        self.realm = Realm(self.map)
        self.realm.found_city((2,2))
    
    def tick(self):
        self.map.tick()

    def start(self):
        print(self.map)
        print("Harvestable resources: ", str(self.realm.get_harvestable_resources()))