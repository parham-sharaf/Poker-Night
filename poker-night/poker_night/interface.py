from deck import *
from player import Player

if __name__ == "__main__":
    logger.info("Welcome to Poker Night")
    logger.info("Enter the number of players playing tonight")
    num_of_player = int(input("Number of player: "))
    logger.info("How much money is each player starting with?")
    idv_share = int(input("Enter the starting money: "))

    players = []
    for player in range(0, num_of_player):
        name_of_player = input("Name of the player: ")
        players.append(Player(name_of_player, idv_share))

    logger.trace("Initializing the cards")
    mydeck = Deck()
    mydeck.build()
    logger.trace("Done initializing the cards")
    logger.debug("Shuffling the cards...")
    mydeck.shuffle()


