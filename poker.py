from card_ids import *

class Card():
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
    

class Hand():
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)
    
    def clear_hand(self):
        self.hand.clear()

    def hand_string(self):
        ret = ""
        ret += ' '.join([get_emoji_top(card.val, card.suit) for card in self.hand])
        ret += ' \n'
        ret += ' '.join([get_emoji_bottom(card.val, card.suit) for card in self.hand])
        return ret

    def hand_value(self):
        