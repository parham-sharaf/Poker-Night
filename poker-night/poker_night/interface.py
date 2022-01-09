from loguru import logger
from game import Game

if __name__ == "__main__":
    logger.trace("Creating a new game")
    game = Game()

    blind_idx = 0           # this changes every round
    game.set_blinds(blind_idx)
    while not game.is_over():
        game.play()
        game.next_round()
