import logging as lg
from logging_config import configure_logging
from utility import str_list, to_dict_resources
from constants import RESSOURCES


class Action:
    def __init__(self, realm, name = "Action", uses_per_turn = 1):
        self.name = name
        self.realm = realm
        self.logger = lg.getLogger(self.name.lower())
        self.uses_left = uses_per_turn
        self.uses_per_turn = uses_per_turn
        
    def get_cost(self, **kwargs):
        return None
    
    def tick(self):
        self.uses_left = self.uses_per_turn

    def activate(self,**kwargs):        
        is_valid = self.is_valid(**kwargs)
        if is_valid:
            self.uses_left -= 1
            self.realm.pay(self.get_cost(**kwargs))
            self.resolve(**kwargs)
            return True
        return False

    def resolve(self, **kwargs):
        self.logger.info(f"Resolving {self.name}")

    def is_valid(self, **kwargs):
        self.logger.info(f"Checking if {self.name} is valid")
        if self.uses_left <= 0:
            self.logger.error(f"[INVALID] Not enough uses left")
            return False
        if not self.realm.can_afford(self.get_cost(**kwargs)):
            self.logger.error(f"[INVALID] Not enough resources")
            return False
        return True
    
class Harvest(Action):
    ## harvests format:
    # [TileResource, TileResource, ...]
    def __init__(self, realm, city):
        super().__init__(realm, name = "Harvest")
        self.city = city

    def is_valid(self, **kwargs):
        if super().is_valid(**kwargs) == False:
            return False
        harvests = kwargs["harvests"]
        left_tiles = list(self.city.tiles)
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
    
    def resolve(self, **kwargs):
        harvests = kwargs["harvests"]
        for resource in harvests:
            self.city.harvest(resource)
            self.logger.info(f"Harvested {resource} from {resource.tile}")
        
class AcquireTile(Action):
    def __init__(self, realm, city):
        super().__init__(realm, name = "AcquireTile")
        self.city = city

    def get_cost(self, **kwargs):
        tile = kwargs["tile"]
        dist = self.city.tile.distance(tile)
        return to_dict_resources(tile.get_cost(dist))
    
    def is_valid(self, **kwargs):
        tile = kwargs["tile"]
        if super().is_valid(**kwargs) == False:
            return False
        if tile in self.city.tiles:
            self.logger.error(f"[INVALID] Tile {tile} already acquired by City")
            return False
        if tile.realm == self.city.realm:
            self.logger.error(f"[INVALID] Tile {tile} already acquired by Realm")
            return False
        self.logger.info(f"[VALID] Acquiring {tile}")
        return True
    
    def resolve(self, **kwargs):
        tile = kwargs["tile"]
        self.city.acquire_tile(tile)

class IncreasePop(Action):
    def __init__(self, realm, city):
        super().__init__(realm, name = "IncreasePop")
        self.city = city

    def get_cost(self):
        return to_dict_resources(self.city.increase_pop_cost())
    
    def is_valid(self):
        if self.city.population >= len(self.city.pop_costs):
            self.logger.error(f"[INVALID] Population already at maximum")
            return False
        if super().is_valid() == False:
            return False
        self.logger.info(f"[VALID] Increasing population")
        return True
    
    def resolve(self):
        self.city.increase_population()

