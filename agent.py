
class Agent:
    def __init__(self, realm):
        self.realm = realm

    def choose_harvests(self):
        return None

    def choose_actions(self):
        actions = {}
        actions["harvests"] = self.choose_harvests()
        return actions

class TestAgent(Agent):
    def choose_harvests(self):
        harvestables = self.realm.get_harvestable_resources()
        if harvestables:
            print(f"Choosing to harvest {harvestables[0][1]} from {harvestables[0][0]}")
            return [harvestables[0]]
        return None