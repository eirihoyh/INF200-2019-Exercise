from ..deck_by_comp import deck_comp



def test_deck_of_cards_have_52_cards():
    assert len(deck_by_comp()) == 52

def test_deck_of_cards_have_4_suits():
    deck = deck_comp()
    suits = {suit for suit, vaue i deck}
    assert len(suits) == 4


# Create a tst to check if there are 13 values
# Create a test to check if there are 52 uniqe cards