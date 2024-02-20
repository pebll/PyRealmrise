from game import LogGame
from logging_config import configure_logging
import logging as lg

configure_logging(level=lg.DEBUG)
mapsize = 7
map_size = (mapsize, mapsize-2)
starting_resources = 2
turns = 10
seed = 1
game = LogGame(mapsize=map_size, starting_resources=starting_resources, turns=turns, seed=seed)
game.start()
