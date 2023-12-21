import re
from enum import Enum

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5','4', '3', '2']
# enum of types

class CardType(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0

def classify_hand(hand):
    # return the type of hand
    hand_set = set(hand)
    if len(set(hand)) <= 2:
        # either full house or four of a kind
        for card in hand_set:
            if hand.count(card) == 5:
                return CardType.FIVE_OF_A_KIND, card
            if hand.count(card) == 4:
                return CardType.FOUR_OF_A_KIND, card
            elif hand.count(card) == 3:
                return CardType.FULL_HOUSE, [card, hand_set.difference(card).pop()]
    elif len(set(hand)) == 3:
        pair_cards = []
        for card in hand_set:
            if hand.count(card) == 3:
                return CardType.THREE_OF_A_KIND, card
            elif hand.count(card) == 2:
                pair_cards.append(card)
            
        return CardType.TWO_PAIR, sorted(pair_cards, key=lambda x: order.index(x))
    elif len(set(hand)) == 4:
        for card in hand_set:
            if hand.count(card) == 2:
                return CardType.PAIR, card
    else:
        return CardType.HIGH_CARD, sorted(hand, key=lambda x: order.index(x))
    

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.classification = classify_hand(hand)
    
    def __lt__(self, other):
        self_card_type = self.classification[0]
        other_card_type = other.classification[0]
        if self_card_type.value == other_card_type.value:
            self_card_value = self.classification[1]
            other_card_value = other.classification[1]
            return self_card_value < other_card_value
        else:
            return self_card_type.value < other_card_type.value
    
    def __repr__(self):
        return f"{self.hand} {self.bid} {self.classification}"

def part_1(lines):
    # read hand and bid
    hands = []
    for line in lines:
        hand, bid = line.split(' ')
        bid = int(bid)
        hand = Hand(hand, bid)
        hands.append(hand)

    # sort by hand classification
    print(hands)
    hands.sort()
    print(hands)
    #print(f"{hand} {bid} {score}")
    #winnings = score*bid
    winnings = sum([hand.bid*(i+1) for i, hand in enumerate(hands)])
    return winnings
    
def part_2(lines):
    total = 0
    return total
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")