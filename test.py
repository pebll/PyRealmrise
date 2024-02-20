from game import LogGame
from logging_config import configure_logging
import logging as lg
from stats import Scenario, run_test_games, average_history, plot_history, compare_scenarios
from agent import TestAgent
import matplotlib.pyplot as plt
import matplotlib as mpl

configure_logging(level=lg.FATAL)
lg.getLogger('matplotlib').setLevel(lg.WARNING)
lg.getLogger('PIL').setLevel(lg.WARNING)
mpl.rcParams['savefig.directory'] = '/home/leo/MEGA/Programmieren/Python/Realmrise/plots'

mapsize = 10
map_size = (mapsize, mapsize)
starting_resources = 0
turns = 150
seed = 10
N = 1

#scenario1= Scenario(name = "Start Res = 0", n = N, mapsize = map_size, starting_resources = 0, turns = turns, seed = seed, agent = TestAgent)


scenarios = []
for i in range(6):
    scenario = Scenario(name = f"Start Res = {i*20}", n = N, mapsize = map_size, starting_resources = i, turns = turns, seed = seed, agent = TestAgent)
    scenarios.append(scenario)

compare_scenarios(scenarios)

    #games = run_test_games(scenario)
#history = average_history(games)
#plot_history(history, keys=["resource_count", "total_population", "total_tiles", "score"])
#plt.show()
#compare_agents(agents, n = N, mapsize = map_size, starting_resources = starting_resources, turns = turns, seed = seed)


#games = run_test_games(n = N,mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
#history = average_history(games)

#plot_history(history, keys=["total_population", "total_tiles"])
#plot_history(history, keys=["resource_count"])

#game = LogGame(mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
#game.start()
