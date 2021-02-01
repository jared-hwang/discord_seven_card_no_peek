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
        self.allDone = 0
        self.pot = 0

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
        self.currLeader.calculate_hand_value()

        for i in range(len(self.players)):
            self.player_dict[self.players[i]] = Player(self.players[i], Hand(card_array=[]))
        self.allDone = len(self.players)

        printArray = [f":arrow_down: {self.currLeader.name} :arrow_down: {self.currLeader.handvalue}", self.currLeader.hand_string()]

        return printArray

    def next_round(self):
        self.roundnum += 1
        
    def flip_player(self, player):
        printArray = []
        if self.player_dict[player].flip == 7 or self.player_dict[player].done:
            printArray.append("You're done!")
            printArray.append(f":arrow_down: {player} :arrow_down: {self.player_dict[player].handvalue}")
            printArray.append(self.player_dict[player].hand.hand_string())
            return printArray
        self.player_dict[player].hand.add_card(self.deck.pop())
        self.player_dict[player].flip += 1
        self.player_dict[player].calculate_hand_value()
        printArray = [f":arrow_down: {player} :arrow_down: {self.player_dict[player].handvalue}", self.player_dict[player].hand.hand_string()]
        if self.currLeader.hand < self.player_dict[player].hand:
            self.currLeader = self.player_dict[player]

        printArray.append(f"{self.currLeader.name} is the current leader with a {self.currLeader.handvalue}")
        if self.player_dict[player].flip == 7 and not self.player_dict[player].done: 
            self.player_dict[player].done = True
            self.allDone -= 1
        
        if self.allDone == 0: # game is over
            printArray.append(f':boom: {self.currLeader.name} is the winner with a {self.currLeader.handvalue}! :boom:')
            self.currLeader.money += self.pot
            self.pot = 0

        return printArray

    def add_to_pot(self, amount):
        self.pot += amount

    def end_game(self):
        currWinner = self.players[0]
        self.player_dict[currWinner].calculate_hand_value()
        for player in self.players[1:]:
            self.player_dict[player].calculate_hand_value()
            if self.player_dict[currWinner].hand < self.player_dict[player].hand:
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

    def fold_player(self, player):
        self.player_dict[player].fold()
        allDone -= 1
        if self.allDone == 1: #game is over
            printArray.append(f':boom: {self.currLeader.name} is the winner with a {self.currLeader.handvalue}! :boom:')
            self.currLeader.money += self.pot
            self.pot = 0
