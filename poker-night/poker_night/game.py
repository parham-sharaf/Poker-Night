#from loguru import logger
from deck import Deck
from player import Player, STATUS, BLIND


class Game:
    def __init__(self):
        self.blind = None
        self.current_player = None
        self.round_num = 0
        print("Welcome to Poker Night")                        
        print("Enter the number of players playing tonight")   
        num_of_player = int(input("Number of player: "))
        print("How much money is each player starting with?")  
        self.idv_share = int(input("Enter the starting money: "))

        self.players = []
        for player in range(0, num_of_player):
            name_of_player = input("Name of the player: ")
            self.players.append(Player(name_of_player, self.idv_share))

        print("Initializing the cards")                          
        my_deck = Deck()
        my_deck.build()
        print ("Done initializing the cards")                   
        print ("Shuffling the cards...")
        my_deck.shuffle()

    def play(self):
        if self.round_num == 0:
            for index in range(len(self.players)):
                if index == self.blind:
                    self.players[index].set_blind(BLIND.SMALL_BLIND)
                    self.players[(index + 1) % len(self.players)].set_blind(BLIND.BIG_BLIND)
                    break
            self.current_player = self.blind + 2

        elif self.round_num == 1:
            self.current_player = (self.current_player + 1) % len(self.players)
            while self.current_player != self.blind + 2:
                print(f"Your turn {self.players[self.current_player].get_name()}: ")
                print("CALL: 1")
                print("RAISE: 2")
                print("FOLD: 3")
                decision = int(input("--: "))
                self.players[self.current_player].set_status(STATUS(decision))

    def is_over(self) -> bool:
        if self.round_num == 5:
            return True
        else:
            folds = 0
            for player in self.players:
                if player.get_status() == STATUS.FOLD:
                    folds = folds + 1
            if folds == len(self.players):
                return True
        return False

    def set_blinds(self, blind):
        self.blind = blind

    def next_round(self):
        self.round_num += 1

    def pass_card(self, cards):
        for player in self.players:
            player.card_one = cards.pop()
            player.card_two = cards.pop()

    def min_bet_amount(self):
        pass


