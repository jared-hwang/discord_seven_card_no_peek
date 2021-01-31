from poker import *


hand = Hand()

for i in range(3, 14):
    hand.add_card(Card(i, "clubs"))
hand.add_card(Card(14, 'clubs'))

print(hand.calculate_hand_value(upto=2))