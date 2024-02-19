import logging as lg
from logging_config import configure_logging
from utility import str_list
import inspect


class Action:
    def __init__(self, realm, name = "Action", base_cost = None, uses_per_turn = 1):
        self.base_cost = base_cost
        self.name = name
        self.realm = realm
        self.logger = lg.getLogger(self.name.lower())
        self.uses_left = uses_per_turn
        self.uses_per_turn = uses_per_turn
        
    def get_cost(self):
        return self.base_cost
    
    def tick(self):
        self.uses_left = self.uses_per_turn

    def activate(self,**kwargs):        
        is_valid = self.is_valid(**kwargs)
        if is_valid:
            self.uses_left -= 1
            #TODO: self.realm.pay(self.get_cost(**kwargs))
            self.resolve(**kwargs)
            return True
        return False

    def resolve(self):
        self.logger.info(f"Resolving {self.name}")

    def is_valid(self):
        self.logger.info(f"Checking if {self.name} is valid")
        if self.uses_left <= 0:
            self.logger.error(f"[INVALID] Not enough uses left")
            return False
        return True

class Harvest(Action):
    ## harvests format:
    # [TileResource, TileResource, ...]
    def __init__(self, realm, city):
        super().__init__(realm, name = "Harvest")
        self.city = city

    def is_valid(self, harvests):
        left_tiles = list(self.city.tiles)

        if super().is_valid() == False:
            return False
        
        if len(harvests) > self.city.population:
            self.logger.error(f"[INVALID]Not enough population to harvest {harvests}")
            return False
        for resource in harvests:
            if resource.tile.realm != self.city.realm:
                self.logger.error(f"[INVALID] Resource {resource} does not belong to the realm")
                return False
            if resource.cooldown > 0:
                self.logger.error(f"[INVALID] Resource {resource} is not ready to be harvested")
                return False
            if resource.tile not in left_tiles:
                self.logger.error((f"[INVALID] Resource {resource} already harvested from on {resource.tile}\n"
                                  f"left tiles: {str_list(left_tiles)}"))
                return False
            else:
                left_tiles.remove(resource.tile)
        self.logger.info(f"[VALID] Harvesting {str_list(harvests)}")
        return True
    
    def resolve(self, harvests):
        for resource in harvests:
            self.city.harvest(resource)
            self.logger.info(f"Harvested {resource} from {resource.tile}")
        
        