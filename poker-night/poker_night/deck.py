#from loguru import logger
from enum import Enum
import random


class SUITS(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.value} of {self.suit}')


class Deck:
    def __init__(self):
        print("Initializing the Deck")
        self.cards = []

    def build(self):
        for suit in [SUITS.HEARTS, SUITS.DIAMONDS, SUITS.CLUBS, SUITS.SPADES]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def display_cards(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_deck(self) -> list:
        return self.cards



