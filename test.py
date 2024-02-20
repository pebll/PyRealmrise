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

mapsize = 10
map_size = (mapsize, mapsize)
starting_resources = 0
turns = 200
seed = 5645
N = 20
decays = [0.1, 0.5, 0.99]
resources = [0,2,6,10]


def compare():
    scenario_random = Scenario(name = f"Agent Random", n = N, mapsize = map_size, starting_resources = starting_resources, turns = turns, seed = seed, agent = BaselineAgent_Random)
    scenarios = []
   
    for decay in decays:
        for resource_count in resources:
            scenario = Scenario(name = f"Agent Hardcoded ({decay}), res: {resource_count}", n = N, mapsize = map_size, starting_resources = resource_count, turns = turns, seed = seed, agent = BaselineAgent_Hardcoded, agent_kwargs={"decays" : decay})
            scenarios.append(scenario)
    for resource_count in resources:
            scenario = Scenario(name = f"Agent Random, res: {resource_count}", n = N, mapsize = map_size, starting_resources = resource_count, turns = turns, seed = seed, agent = BaselineAgent_Hardcoded)
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
