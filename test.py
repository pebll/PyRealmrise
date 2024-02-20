from game import LogGame
from logging_config import configure_logging
import logging as lg
from stats import *


configure_logging(level=lg.WARNING)
lg.getLogger('matplotlib').setLevel(lg.WARNING)
lg.getLogger('PIL').setLevel(lg.WARNING)


mapsize = 7
map_size = (mapsize, mapsize)
starting_resources = 0
turns = 20
seed = 0
N = 100
games = run_test_games(n = N,mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
history = average_history(games)

plot_history(history, keys=["total_population", "total_tiles"])
#plot_history(history, keys=["resource_count"])

#game = LogGame(mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
#game.start()
