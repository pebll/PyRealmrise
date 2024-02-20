from game import LogGame
from logging_config import configure_logging
import logging as lg
from stats import Scenario, run_log_game, average_history, plot_history, compare_scenarios
from baselines import BaselineAgent_Random, BaselineAgent_Hardcoded
import matplotlib.pyplot as plt
import matplotlib as mpl

configure_logging(level=lg.FATAL)
lg.getLogger('matplotlib').setLevel(lg.WARNING)
lg.getLogger('PIL').setLevel(lg.WARNING)

mpl.rcParams['savefig.directory'] = '/home/leo/MEGA/Programmieren/Python/Realmrise/plots'

mapsize = 5
map_size = (mapsize, mapsize)
starting_resources = 5
turns = 10
seed = 5
N = 10
decays = [0.3, 0.5, 0.7]

def compare():
    scenario_random = Scenario(name = f"Agent Random", n = N, mapsize = map_size, starting_resources = starting_resources, turns = turns, seed = seed, agent = BaselineAgent_Random)
    scenarios = [scenario_random]
    for i in range(0):
        scenario = Scenario(name = f"Agent Hardcoded ({decays[i]})", n = N, mapsize = map_size, starting_resources = starting_resources, turns = turns, seed = seed, agent = BaselineAgent_Hardcoded)#, agent_kwargs={"decays" : decays[i]})
        scenarios.append(scenario)

    compare_scenarios(scenarios)

def log_run():
    lg.getLogger('root').setLevel(lg.INFO)
    scenario = Scenario(name = f"Agent Random", n = N, mapsize = map_size, starting_resources = starting_resources, turns = turns, seed = seed, agent = BaselineAgent_Random)
    game = run_log_game(scenario)

compare()
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
