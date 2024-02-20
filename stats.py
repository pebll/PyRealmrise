from game import TestGame
import matplotlib.pyplot as plt
import numpy as np
import random

SMOOTHNESS = 100  # Adjust the number of points for smoother interpolation

class Scenario():
    def __init__(self, name = "Scenario", n = 1, mapsize = (5,5), starting_resources = 2, turns = 10, seed = 1, agent = None):
        self.name = name
        self.mapsize = mapsize
        self.starting_resources = starting_resources
        self.turns = turns
        self.seed = seed
        self.agent = agent
        self.n = n

    def to_dict(self):
        return {"n":self.n, "mapsize": self.mapsize, "starting_resources": self.starting_resources, "turns": self.turns, "seed": self.seed, "agent": self.agent}

    def to_game_config(self):
        return {"mapsize": self.mapsize, "starting_resources": self.starting_resources, "turns": self.turns, "seed": self.seed, "agent": self.agent}
    
    def tick_seed(self):
        if self.seed:
            self.seed += 1
    
    def copy(self):
        return Scenario(n = self.n, mapsize = self.mapsize, starting_resources = self.starting_resources, turns = self.turns, seed = self.seed, agent = self.agent)


def run_test_game(scenario):
    game = TestGame(**scenario.to_game_config())
    game.start()
    return game

def run_test_games(scenario):
    scenario = scenario.copy()
    games = []
    for _ in range(scenario.n):
        scenario.tick_seed()
        games.append(run_test_game(scenario))
    return games

def average_history(games):
    history = games[0].history
    for game in games[1:]:
        for key in history.keys():
            history[key] = [a + b for a, b in zip(history[key], game.history[key])]
    for key in history.keys():
        history[key] = [val / len(games) for val in history[key]]
    return history

def plot_history(history, keys = None, label = None):
    if keys:
        history = {key: history[key] for key in keys}
    if label and len(keys) == 1:
        values = list(history.values())[0]
        x_smooth = np.linspace(0, len(values) - 1, SMOOTHNESS)
        y_smooth = np.interp(x_smooth, range(len(values)), values)
        plt.plot(x_smooth, y_smooth, linewidth = 3, label=label)
    else:
        for key, values in history.items():
            x_smooth = np.linspace(0, len(values) - 1, SMOOTHNESS)
            y_smooth = np.interp(x_smooth, range(len(values)), values)
            plt.plot(x_smooth, y_smooth, linewidth = 3, label=key)  # Smooth curve with markers
    plt.xlabel('Turns')
    plt.ylabel('Values')
    plt.title('Game History')
    plt.legend()
    plt.grid(True)

def compare_scenarios(scenarios):
    scenario_histories = {}
    for i, scenario in enumerate(scenarios):
        print(f"Running scenario {i+1}/{len(scenarios)}: {scenario.name}")   
        games = run_test_games(scenario)
        scenario_histories[scenario.name] = average_history(games)
    for scenario, history in scenario_histories.items():
        plot_history(history, keys=["score"], label=scenario)
    plt.show()