import re
from enum import Enum

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5','4', '3', '2']

order_pt2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5','4', '3', '2', 'J']
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
    

import itertools

def classify_hand_pt_2(hand):
    # return the type of hand
    hand_set = set(hand)
    joker = False
    num_jokers = hand.count('J')

    if 'J' in hand_set:
        joker = True

    # determine original hand score
    best_classification = classify_hand(hand)
    # get all joker indices
    
    joker_indexes = [i for i, card in enumerate(hand) if card == 'J']

    # brute force approach: replace each joker with a different card
    for perm in itertools.product(order_pt2, repeat=num_jokers):
        # make a copy of the hand
        perm_hand = list(hand)
        # update the hand based on the permutation
        for i, joker_index in enumerate(joker_indexes):
            perm_hand[joker_index] = perm[i]

        # evaluate the hand
        classification = classify_hand(perm_hand)
        if classification[0].value > best_classification[0].value:
            best_classification = classification
        elif classification[0].value == best_classification[0].value:
            if classification[1] > best_classification[1]:
                best_classification = classification

    return best_classification


class Hand:
    def __init__(self, hand, bid, type='pt1'):
        self.hand = hand
        self.bid = bid
        if type == 'pt1':
            self.classification = classify_hand(hand)
            self.order = order
        else: 
            self.classification = classify_hand_pt_2(hand)
            self.order = order_pt2
    
    def __lt__(self, other):
        self_card_type = self.classification[0]
        other_card_type = other.classification[0]
        if self_card_type.value == other_card_type.value:
            # map hand to order values
            reverse_order = list(reversed(self.order))
            self_hand = [reverse_order.index(card) for card in self.hand]
            other_hand = [reverse_order.index(card) for card in other.hand]

            # compare hands using order
            return self_hand < other_hand
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
    #print(hands)
    hands.sort()
    #print(hands)
    #print(f"{hand} {bid} {score}")
    #winnings = score*bid
    winnings = sum([hand.bid*(i+1) for i, hand in enumerate(hands)])
    return winnings
    
def part_2(lines):
    # read hand and bid
    hands = []
    for line in lines:
        hand, bid = line.split(' ')
        bid = int(bid)
        hand = Hand(hand, bid, type='pt2')
        hands.append(hand)

    # sort by hand classification
    #print(hands)
    hands.sort()
    #print(hands)
    #print(f"{hand} {bid} {score}")
    #winnings = score*bid
    winnings = sum([hand.bid*(i+1) for i, hand in enumerate(hands)])
    return winnings
    

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