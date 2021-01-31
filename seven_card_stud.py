from card_game import *
from poker import *
from card_ids import *
import math, random

class SevenCardNoPeek(Game):
    def __init__(self):
        super().__init__()
        self.deck = []
        self.roundnum = 0
        self.player_dict = {}
        self.dealerhand = None
        self.currLeader = None

    def initialize_game(self):
        self.roundnum = 0
        num_decks = math.ceil((len(self.players) * 7)/52)

        for deck in range(num_decks):
            for suit in ['clubs', 'diamonds', 'hearts', 'spades']:
                for val in range(2, 15):
                    self.deck.append(Card(val, suit))

        random.shuffle(self.deck)
        self.dealerhand = Hand(card_array=[self.deck.pop()])
        self.currLeader = Player("DealerBot", self.dealerhand)

        for i in range(len(self.players)):
            self.player_dict[self.players[i]] = Hand(card_array=self.deck[7*i:(7*i)+7])


    def next_round(self):
        self.roundnum += 1

    def end_game(self):
        currWinner = self.players[0]
        self.player_dict[currWinner].calculate_hand_value()
        for player in self.players[1:]:
            if self.player_dict[currWinner] < self.player_dict[player]:
                currWinner = player
        winMessage = "@{} wins with a {}!".format(currWinner, self.player_dict[currWinner].handvalue)
        return winMessage

    def reset_game(self):
        for playername, playerhand in self.player_dict.items():
            playerhand.clear_hand()
        self.player_dict.clear()
        self.players.clear()
        self.deck.clear()
        self.roundnum = 0

