from resources import Resource

class Action:
    def __init__(self, base_cost):
        self.base_cost = base_cost
        
    def add_costs(self, costs):
        for cost in costs:
            self.cost[str(cost)] += 1
    
    def activate(self, realm, map):
        pass

