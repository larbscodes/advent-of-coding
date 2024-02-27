import functools 

with open('7-camel-cards-input.txt') as input:

    def card_to_value(a):
        if a == 'T':
            return 10
        elif a == 'J':
            return -1
        elif a == 'Q':
            return 12
        elif a == 'K':
            return 13
        elif a == 'A':
            return 14
        else:
            return int(a)
    
    def hand_to_value(a):
        existing_cards_dict = {}
        for card in a[0]:
            number_cards = existing_cards_dict.get(card, 0)
            if number_cards == 0:
                existing_cards_dict[card] = 1
            else:
                existing_cards_dict[card] += 1
        num_jokers = existing_cards_dict.get('J', 0)
        has_jokers = num_jokers > 0
        num_keys = len(existing_cards_dict.keys())
        if has_jokers:
            num_keys -= 1

        existing_cards_dict['J'] = 0
        largest_value = max(list(existing_cards_dict.values()))
        num_matching_cards = largest_value + num_jokers

        if num_keys <= 1:
            return 6
        elif num_keys == 2:
            if num_matching_cards == 4:
                return 5
            else:
                return 4
        elif num_keys == 3:
            if num_matching_cards == 3:
                return 3
            else:
                return 2
        elif num_keys == 4:
            return 1
        else:
            return 0

    def compare_cards(a, b):
        hand1 = a[0]
        hand2 = b[0]
        for i in range(0, 5):
            if card_to_value(hand1[i]) < card_to_value(hand2[i]):
                return -1
            elif card_to_value(hand1[i]) > card_to_value(hand2[i]):
                return 1
            else:
                continue
        return 0
    
    def compare_hands(a, b):
        if hand_to_value(a) < hand_to_value(b):
            return -1
        elif hand_to_value(a) > hand_to_value(b):
            return 1
        else:
            return compare_cards(a, b)

    hands = []
    for line in input:
        array = line.split(' ')
        hands.append((array[0], int(array[1].strip())))
    
    hands.sort(key=functools.cmp_to_key(compare_hands))
    print(hands)
    winnings = 0
    for i, hand in enumerate(hands):
        multiplier = i + 1
        winning = hand[1] * multiplier
        winnings += winning
    
    print(winnings)