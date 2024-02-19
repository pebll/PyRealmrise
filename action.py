import logging as lg
from logging_config import configure_logging


class Action:
    def __init__(self, realm, name = "Action", base_cost = None, uses_per_turn = 1):
        self.base_cost = base_cost
        self.name = name
        self.realm = realm
        self.logger = lg.getLogger(self.name.lower())
        self.uses_left = uses_per_turn
        self.uses_per_turn = uses_per_turn
        configure_logging(self.name.lower())
        
    def get_cost(self):
        return self.base_cost
    
    def tick(self):
        self.uses_left = self.uses_per_turn

    def activate(self,**kwargs):
        self.uses_left -= 1
        if self.is_valid(kwargs):
            self.realm.pay(self.get_cost(kwargs))
            self.resolve(kwargs)
            return True
        return False

    def resolve(self):
        self.logger.info(f"Resolving {self.name}")

    def is_valid(self):
        return True

class Harvest(Action):
    ## harvests format:
    # [TileResource, TileResource, ...]
    def __init__(self, city):
        super().__init__("Harvest")
        self.city = city

    def activate(self, harvests):
        super().activate(harvests=harvests)

    def is_valid(self, harvests):
        left_tiles = self.city.tiles
        if len(harvests) > self.city.population:
            self.logger.error(f"[INVALID]Not enough population to harvest {harvests}")
            return False
        for resource in harvests:
            if resource.realm != self.city.realm:
                self.logger.error(f"[INVALID] Resource {resource} does not belong to the realm")
                return False
            if resource.countdown > 0:
                self.logger.error(f"[INVALID] Resource {resource} is not ready to be harvested")
                return False
            if resource.tile not in left_tiles:
                self.logger.error(f"[INVALID] Resource {resource} already harvested from on {resource.tile}")
                return False
            else:
                left_tiles.remove(resource.tile)
        self.logger.info(f"[VALID] Harvesting {harvests}")
        return True
    
    def resolve(self, harvests):
        for resource in harvests:
            self.city.harvest(resource)
            self.logger.info(f"Harvested {resource} from {resource.tile}")
        
        