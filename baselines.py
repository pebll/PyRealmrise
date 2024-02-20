from agent import Agent
from random import shuffle, choice
from utility import str_list, add_to_dict_resources
import math


class BaselineAgent_Random(Agent):
    def choose_pop(self):
        for city in self.realm.cities:
            if self.realm.can_afford(city.increase_pop_cost()):
                self.logger.info(f"Chose to increase population")
                self.actions.append((city.actions["increase_pop"], {}))
                return True

    def choose_tile(self):
        for city in self.realm.cities:
            action = city.actions["acquire_tile"]
            possible_tiles = []
            tiles = city.acquirable_tiles()
            if tiles:
                for tile in tiles:
                    if action.is_valid(tile=tile):
                            possible_tiles.append(tile)
            if possible_tiles:
                tile = choice(possible_tiles)
                self.logger.info(f"Chose to acquire tile {tile}")
                self.actions.append((city.actions["acquire_tile"], {"tile": tile}))
                return True
                
    def choose_actions(self):
        self.actions = []
        self.choose_tile()
        self.choose_pop()
        self.choose_harvests()
        return self.actions
    
    def choose_harvests(self):
        for city in self.realm.cities:
            left_tiles = shuffle(list(city.tiles))
            harvests = []
            for _ in range(city.population):
                while left_tiles:
                    tile = left_tiles.pop()
                    resources = shuffle(tile.available_resources())
                    if resources:
                        harvests.append(resources[0])
                        break
            if harvests:
                self.logger.info(f"Chose to harvest {str_list(harvests)}")
                self.actions.append((city.actions["harvest"], {"harvests": harvests}))

class BaselineAgent_Hardcoded(BaselineAgent_Random):
    def __init__(self, realm, decay=0.5):
        self.decay = decay
        super().__init__(realm)
    def choose_tile(self):
        for city in self.realm.cities:
            action = city.actions["acquire_tile"]
            possible_tiles = []
            tiles = city.acquirable_tiles()
            if tiles:
                for tile in tiles:
                    if action.is_valid(tile=tile):
                            possible_tiles.append(tile)
            if possible_tiles:
                ## 
                cov = self.realm.get_resource_coverage()
                best_score = self.get_cov_score(cov)
                best_tile = None
                for tile in possible_tiles:
                    new_cov = add_to_dict_resources(cov, tile.type.resources)
                    score = self.get_cov_score(new_cov)
                    if score > best_score:
                        best_score = score
                        best_tile = tile
                tile = best_tile
                ##
                self.logger.info(f"Chose to acquire tile {tile}")
                self.actions.append((city.actions["acquire_tile"], {"tile": tile}))
                return True
    
    def get_cov_score(self, cov):
        return sum([math.pow(cov[res], self.decay) for res in cov])
    
    def choose_harvests(self):
        return super().choose_harvests()