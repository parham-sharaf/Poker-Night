from enum import IntEnum


class STATUS(IntEnum):
    CALL = 0
    RAISE = 1
    FOLD = 2
    CHECK = 3
    READY = 4


class BLIND(IntEnum):
    OTHER = 0
    BIG_BLIND = 1
    SMALL_BLIND = 2


class Player:
    def __init__(self, name, money):
        self.blind = None
        self.status = STATUS.READY
        self.card_one = None
        self.card_two = None
        self.name = name
        self.total_money = money

    def get_name(self) -> str:
        return self.name

    def all_in(self) -> int:
        money = self.total_money
        self.total_money = 0
        return money

    def hold_cards(self, cards):
        self.card_one = cards[0]
        self.card_two = cards[1]

    def set_status(self, status):
        self.status = status

    def get_status(self) -> STATUS:
        return self.status
    
    def set_blind(self, blind):
        self.blind = blind
    
    def get_blind(self) -> BLIND:
        return self.blind

