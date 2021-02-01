from card_ids import *

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.flip = 0
        self.handvalue = ''
        self.done = False
        self.money = 2000

    def flipme(self):
        self.flip += 1
        self.handvalue = self.hand.calculate_hand_value(upto=self.flip)
        
    def calculate_hand_value(self):
        self.handvalue = self.hand.calculate_hand_value()
        return self.handvalue

    def clear_hand(self):
        self.hand.clear_hand()
    
    def hand_string(self):
        return self.hand.hand_string()

    def bet(self, amount):
        self.money -= amount

    def fold(self):
        self.done = True

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
        self.max_of_hand_combo = 0
        self.last_hand_calculated = 0

    def __lt__(self, other):
        if self.handvalue == '':
            self.handvalue = self.calculate_hand_value()
        if other.handvalue == '':
            other.handvalue = other.calculate_hand_value()

        if hand_order[self.handvalue] == hand_order[other.handvalue]:
            get_higher = self.compare_same_hand(self, other, self.handvalue)
            if get_higher == 1:
                return False
            else: 
                return True
        else:
            return hand_order[self.handvalue] < hand_order[other.handvalue]

    def __gt__(self, other):
        if self.handvalue == '':
            self.handvalue = self.calculate_hand_value()
            print(self.handvalue, self.max_of_hand_combo)
        if other.handvalue == '':
            other.handvalue = other.calculate_hand_value()
            print(other.handvalue, other.max_of_hand_combo)

        if hand_order[self.handvalue] == hand_order[other.handvalue]:
            get_higher = self.compare_same_hand(self, other, self.handvalue)
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
            get_higher = self.compare_same_hand(self, other, self.handvalue)
            if get_higher == 1 or get_higher == 2:
                return False
            else: 
                return True
        else:
            return False

    def greater_high_card(self, hand1, hand2):
            hand1sorted = list(reversed(sorted(hand1.hand)))
            hand2sorted = list(reversed(sorted(hand2.hand)))
            minlength = min(len(hand1sorted), len(hand2sorted))
            for i in range(minlength):
                if hand1sorted[i] > hand2sorted[i]:
                    return 1
                elif hand2sorted[i] > hand1sorted[i]:
                    return 2
            if len(hand1sorted) != len(hand2sorted):
                if len(hand1sorted) > len(hand2sorted):
                    return 1
                elif len(hand2sorted) > len(hand1sorted):
                    return 2
            return 0

    # 1 if hand1 is greater, 2 if hand2 is greater, 0 of completely equal
    def compare_same_hand(self, hand1, hand2, handtype): 
        if handtype == "royal flush":
            return self.greater_high_card(hand1, hand2)
        elif handtype == 'straight flush' or handtype == 'four of a kind' or \
             handtype == 'flush' or handtype == 'straight' or \
             handtype == 'three of a kind' or handtype == 'pair':
            if hand1.max_of_hand_combo > hand2.max_of_hand_combo:
                return 1
            elif hand2.max_of_hand_combo > hand1.max_of_hand_combo:
                return 2
        elif handtype == 'full house' or handtype == 'two pair':
            if hand1.max_of_hand_combo[0] > hand2.max_of_hand_combo[0]:
                return 1
            elif hand2.max_of_hand_combo[0] > hand1.max_of_hand_combo[0]:
                return 2
            elif hand1.max_of_hand_combo[1] > hand2.max_of_hand_combo[1]:
                return 1
            elif hand2.max_of_hand_combo[1] > hand1.max_of_hand_combo[1]:
                return 2

        return self.greater_high_card(hand1, hand2)

        
    def add_card(self, card):
        self.hand.append(card)
    
    def clear_hand(self):
        self.hand.clear()

    def hand_string(self, upto=None):
        if len(self.hand) == 0:
            return "[No cards]"
        if upto is None: upto = len(self.hand)
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
        if upto is None: upto = len(self.hand)
        if upto == self.last_hand_calculated: return self.handvalue
        self.handvalue, self.max_of_hand_combo = self.hand_value(self.hand[:upto])
        self.last_hand_calculated = upto
        return self.handvalue

    def hand_value(self, hand):
        royal_flush, straight_flush = False, False
        # is Straight
        straight, maxStraightVal = self.isStraight(hand)
        maxSameSuitVal = 0
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
            return ("royal flush", 14)
        elif straight_flush:
            return ("straight flush", maxSameSuitVal)

        # n of a kind hands
        fourofakind, threeofakind, twopair, pair, fullhouse = False, False, False, False, False
        counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
        for card in hand:
            counts[card.val] += 1
        
        pairmax = 0
        twopairmax = 0
        threeofakindmax = 0
        fourofakindmax = 0
        for num in range(2, 15):
            val = counts[num]
            if val == 2:
                if pair and twopair:
                    pairmax = twopairmax
                    twopairmax = num
                elif pair: 
                    twopair = True
                    twopairmax = num
                else: 
                    pair = True
                    pairmax = num
            if val == 3:
                threeofakind = True
                threeofakindmax = num
            if val == 4:
                fourofakind = True
                fourofakindmax = num
            
        if fourofakind: 
            return ("four of a kind", fourofakindmax)
        elif threeofakind and pair: # full house
            return ("full house", [threeofakindmax, max(pairmax, twopairmax)])
        
        # flush
        suits = {'spades': 0, 'diamonds': 0, 'hearts': 0, 'clubs': 0}
        flush = False
        flushmax = 0
        for card in hand:
            suits[card.suit] += 1
        
        for suit, count in suits.items():
            if count >= 5:
                flush = True
                for card in hand:
                    if card.suit == suit:
                        flushmax = max(card.val, flushmax)
        if flush: 
            return ("flush", flushmax)
        elif straight: 
            return ("straight", maxStraightVal)
        elif threeofakind:
            return ("three of a kind", threeofakindmax)
        elif twopair:
            return ("two pair", [twopairmax, pairmax])
        elif pair:
            return ("pair", pairmax)
        else:
            return ("high card", 0)

