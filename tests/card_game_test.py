import unittest as unittest

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 7)
        self.card2 = Card("Clubs", 4)
        self.card_game_01 = CardGame(self.card1, self.card2)

    def test_card_has_suit(self):
        pass

