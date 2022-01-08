from deck import Card
from enum import Enum


class Status(Enum):
    CALL = 1
    RAISE = 0
    FOLD = 2
    CHECK = 3


class Player:
    def __init__(self, name, money):
        self.card_one = None
        self.card_two = None
        self.name = name
        self.total_money = money

    def all_in(self) -> int:
        money = self.total_money
        self.total_money = 0
        return money

    def hold_cards(self, cards):
        self.card_one = cards[0]
        self.card_two = cards[1]

