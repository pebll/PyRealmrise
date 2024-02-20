from game import LogGame
from logging_config import configure_logging
import logging as lg
from stats import compare_agents, Scenario, run_test_games, average_history, plot_history, compare_scenarios
from agent import TestAgent
import matplotlib.pyplot as plt


configure_logging(level=lg.WARNING)
lg.getLogger('matplotlib').setLevel(lg.WARNING)
lg.getLogger('PIL').setLevel(lg.WARNING)


mapsize = 5
map_size = (mapsize, mapsize)
starting_resources = 0
turns = 100
seed = 10
N = 10
agents = [TestAgent, TestAgent]

scenario1= Scenario(name = "Start Res = 0", n = N, mapsize = map_size, starting_resources = 0, turns = turns, seed = seed, agent = TestAgent)
scenario2= Scenario(name = "Start Res = 2", n = N, mapsize = map_size, starting_resources = 2, turns = turns, seed = seed, agent = TestAgent)
scenario3= Scenario(name = "Start Res = 4", n = N, mapsize = map_size, starting_resources = 4, turns = turns, seed = seed, agent = TestAgent)
scenario4= Scenario(name = "Start Res = 10", n = N, mapsize = map_size, starting_resources = 10, turns = turns, seed = seed, agent = TestAgent)

scenarios = [scenario1, scenario2, scenario3, scenario4]
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
