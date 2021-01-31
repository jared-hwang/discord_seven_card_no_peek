from card_ids import *

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.flip = 0
        self.handvalue = ''

    def flipme(self):
        self.flip += 1
        self.handvalue = self.hand.calculate_hand_value(upto=self.flip)

class Card():
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        return str((self.val, self.suit))

    def __str__(self):
        return self.__repr__()

    def __lt__(self, other):
        return self.val < other.val
    def __le__(self, other):
        return self.val <= other.val
    def __eq__(self, other):
        return self.val == other.val
    def __gt__(self, other):
        return self.val > other.val
    def __ge__(self, other):
        return self.val >= other.val
    def __ne__(self, other):
        return self.val != other.val
    def __hash__(self):
        return hash(self.val)


class Hand():
    def __init__(self, card_array=[]):
        if len(card_array) != 0:
            self.hand = card_array
        else:
            self.hand = []
        
        self.handvalue = ''

    def __lt__(self, other):
        if self.handvalue == '':
            self.handvalue = self.calculate_hand_value()
        if other.handvalue == '':
            other.handvalue = other.calculate_hand_value()

        if hand_order[self.handvalue] == hand_order[other.handvalue]:
            get_higher = self.greater_high_card(self, other)
            if get_higher == 1:
                return False
            else: 
                return True
        else:
            return hand_order[self.handvalue] < hand_order[other.handvalue]

    def __gt__(self, other):
        if self.handvalue == '':
            self.handvalue = self.calculate_hand_value()
        if other.handvalue == '':
            other.handvalue = other.calculate_hand_value()

        if hand_order[self.handvalue] == hand_order[other.handvalue]:
            get_higher = self.greater_high_card(self, other)
            if get_higher == 1:
                return True
            else: 
                return False
        else:
            return hand_order[self.handvalue] > hand_order[other.handvalue]

    def __eq__(self, other):
        if self.handvalue == '':
            self.handvalue = self.calculate_hand_value()
        if other.handvalue == '':
            other.handvalue = other.calculate_hand_value()
        if hand_order[self.handvalue] == hand_order[other.handvalue]:
            get_higher = self.greater_high_card(self, other)
            if get_higher == 1 or get_higher == 2:
                return False
            else: 
                return True
        else:
            return False


    def greater_high_card(self, hand1, hand2):
        hand1sorted = list(reversed(sorted(hand1)))
        hand2sorted = list(reversed(sorted(hand2)))
        minlength = min(len(hand1sorted), len(hand2sorted))
        for i in range(minlength):
            if hand1sorted[i] > hand2sorted[i]:
                return 1
            elif hand2sorted[i] > hand1sorted[i]:
                return 2
        if len(hand1sorted) != len(hand2sorted):
            if len(hand1sorted) > len(hand2sorted):
                return 1
            else:
                return 2
        return 0
        
    def add_card(self, card):
        self.hand.append(card)
    
    def clear_hand(self):
        self.hand.clear()

    def hand_string(self, upto):
        ret = ""
        ret += ' '.join([get_emoji_top(card.val, card.suit) for card in self.hand[:upto]])
        ret += ' \n'
        ret += ' '.join([get_emoji_bottom(card.val, card.suit) for card in self.hand[:upto]])
        return ret

    def isStraight(self, hand):
        if len(hand) == 0: return (False, 0)
        sorted_hand = sorted(set(hand))
        maxStraightLength, currStraightLength = 1, 1
        maxValue, minValue = sorted_hand[0].val, sorted_hand[0].val
        maxPos, minPos = 1, 1
        for i in range(1, len(sorted_hand)):
            if sorted_hand[i].val-1 == sorted_hand[i-1].val:
                currStraightLength += 1
                if currStraightLength >= maxStraightLength:
                    maxStraightLength = currStraightLength
                    maxValue, maxPos = sorted_hand[i].val, i
                    minValue, minPos = sorted_hand[i-(currStraightLength-1)].val, i-(currStraightLength-1)
            else:
                currStraightLength = 0
        if minValue == 2:
            if sorted_hand[-1].val == 14:
                maxStraightLength += 1
                minValue = 1
        return (maxStraightLength >= 5, maxValue)

    def isSameSuit(self, hand):
        if len(hand) == 0: return True
        suit = hand[0].suit
        for card in hand:
            if card.val != suit:
                return False
        return True

    def calculate_hand_value(self, upto=None):
        if upto is None: upto = len(self.hand)-1
        self.handvalue = self.hand_value(self.hand[:upto+1])
        return self.handvalue

    def hand_value(self, hand):
        royal_flush, straight_flush = False, False
        # is Straight
        straight, maxStraightVal = self.isStraight(hand)
        if straight: # I'm a straight!
            # royal flush, straight flush, straight
            suits = {'spades': [], 'diamonds': [], 'hearts': [], 'clubs': []}
            for card in hand:
                suits[card.suit].append(card)
            maxSameSuitVal = 0
            for val in suits.values():
                suitStraight, suitmax = self.isStraight(val)
                if suitStraight:
                    maxSameSuitVal = max(maxSameSuitVal, suitmax)
                    straight_flush = True
                    if suitmax == 14:
                        royal_flush = True
        if royal_flush:
            return "royal flush"
        elif straight_flush:
            return "straight flush"

        # n of a kind hands
        fourofakind, threeofakind, twopair, pair, fullhouse = False, False, False, False, False
        counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
        for card in hand:
            counts[card.val] += 1
        
        for num, val in counts.items():
            if val == 2:
                if pair: twopair = True
                else: pair = True
            if val == 3:
                threeofakind = True
            if val == 4:
                fourofakind = True
            
        if fourofakind: 
            return "four of a kind" 
        elif threeofakind and pair: # full house
            return "full house"
        
        # flush
        suits = {'spades': 0, 'diamonds': 0, 'hearts': 0, 'clubs': 0}
        flush = False
        for card in hand:
            suits[card.suit] += 1
            if suits[card.suit] == 5:
                flush = True
                return "flush"
        
        if straight: 
            return "straight"
        elif threeofakind:
            return "three of a kind"
        elif twopair:
            return "two pair"
        elif pair:
            return "pair"
        else:
            return "high card"

