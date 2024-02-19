from game import Game
from logging_config import configure_logging
import logging as lg

configure_logging(level=lg.DEBUG)
game = Game()
game.start()
