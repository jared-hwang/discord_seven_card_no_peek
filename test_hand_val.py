from poker import *


hand = Hand()

for i in range(3, 14):
    hand.add_card(Card(i, "clubs"))
hand.add_card(Card(14, 'clubs'))

print(hand.calculate_hand_value())
print(hand.max_of_hand_combo)


hand1 = Hand()
hand1.add_card(Card(8, "spades"))
hand1.add_card(Card(3, "diamonds"))
hand1.add_card(Card(10, "diamonds"))
hand1.add_card(Card(3, "clubs"))

hand2 = Hand()
hand2.add_card(Card(3, "diamonds"))
hand2.add_card(Card(2, "hearts"))
hand2.add_card(Card(5, "diamonds"))
hand2.add_card(Card(3, "hearts"))
hand2.add_card(Card(6, "clubs"))

hand3 = Hand()
hand3.add_card(Card(3, "spades"))
hand3.add_card(Card(6, "diamonds"))
hand3.add_card(Card(8, "clubs"))
hand3.add_card(Card(5, "diamonds"))
hand3.add_card(Card(2, "diamonds"))
hand3.add_card(Card(12, "diamonds"))
hand3.add_card(Card(7, "spades"))
print(hand3.calculate_hand_value())