import unittest as unittest

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Clubs", 4)
        self.card_game_01 = CardGame(self.card1, self.card2)

    def test_game_has_card_01(self):
        pass

    def test_game_has_card_02(self):
        pass

    def test_can_check_for_ace(self):
        pass


    def test_can_find_highest_card(self):
        pass


    def test_can_calculate_total(self):
        pass
