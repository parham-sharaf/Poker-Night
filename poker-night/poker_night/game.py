from loguru import logger
from player import Player
from enum import Enum


class STATUS(Enum):
    CALL = 1
    RAISE = 0
    FOLD = 2
    CHECK = 3


class Game:
    def __init__(self):
        self.round_num = None
        logger.info("Welcome to Poker Night")
        logger.info("Enter the number of players playing tonight")
        num_of_player = int(input("Number of player: "))
        logger.info("How much money is each player starting with?")
        self.idv_share = int(input("Enter the starting money: "))

        self.players = []
        for player in range(0, num_of_player):
            name_of_player = input("Name of the player: ")
            self.players.append(Player(name_of_player, self.idv_share))

    def is_over(self) -> bool:
        if self.round_num == 5:
            return True
        else:
            folds = 0
            for player in self.players:
                if player.status() == STATUS.FOLD:
                    folds = folds + 1
            if folds == self.players.count():
                return True
        return False

    def next_round(self):
        self.round_num += 1

    def min_bet_amount(self):
        pass


