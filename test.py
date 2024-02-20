from game import LogGame
from logging_config import configure_logging
import logging as lg

configure_logging(level=lg.DEBUG)
mapsize = 5
map_size = (mapsize, mapsize)
starting_resources = 3
turns = 10
seed = 1
game = LogGame(mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
game.start()
