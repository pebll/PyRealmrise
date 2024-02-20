from game import TestGame
import matplotlib.pyplot as plt
import numpy as np

SMOOTHNESS = 100  # Adjust the number of points for smoother interpolation

def run_test_game(mapsize = (5,5), starting_resources = 2, turns = 10, seed = 1):
    game = TestGame(mapsize=mapsize, starting_resources=starting_resources, turns=turns, seed=seed)
    game.start()
    return game

def run_test_games(n=10, mapsize = (5,5), starting_resources = 2, turns = 10, seed = 1):
    games = [run_test_game(mapsize=mapsize, starting_resources=starting_resources, turns=turns, seed=seed+i) for i in range(n)]
    return games

def average_history(games):
    history = games[0].history
    for game in games[1:]:
        for key in history.keys():
            history[key] = [a + b for a, b in zip(history[key], game.history[key])]
    for key in history.keys():
        history[key] = [val / len(games) for val in history[key]]
    return history

def plot_history(history, keys = None):
    if keys:
        history = {key: history[key] for key in keys}
    for key, values in history.items():
        x_smooth = np.linspace(0, len(values) - 1, SMOOTHNESS)
        y_smooth = np.interp(x_smooth, range(len(values)), values)
        plt.plot(x_smooth, y_smooth, linewidth = 3, label=key)  # Smooth curve with markers
    plt.xlabel('Turns')
    plt.ylabel('Values')
    plt.title('Game History')
    plt.legend()
    plt.grid(True)
    plt.show()

