from deck import Card


class Player:
    def __init__(self, name, money):
        self.status = None
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

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
