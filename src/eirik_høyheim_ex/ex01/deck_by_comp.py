SUITS = ("C", "S", "H", "D")
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """Takes in suits and values and makes a list of the whole deck"""
    return [(letters, values) for letters in SUITS for values in VALUES]


if __name__ == "__main__":
    if deck_loop() != deck_comp():
        print("ERROR!")
