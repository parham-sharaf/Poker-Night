from deck import *
from player import Player

if __name__ == "__main__":



    logger.trace("Initializing the cards")
    mydeck = Deck()
    mydeck.build()
    logger.trace("Done initializing the cards")
    logger.debug("Shuffling the cards...")
    mydeck.shuffle()

    num_of_rounds = 0
