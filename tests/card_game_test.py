import unittest as unittest

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 4)
        self.card2 = Card("Clubs", 1)
        self.card_game_01 = CardGame(self.card1, self.card2)

    def test_game_has_card_01(self):
        self.assertEqual(self.card1, self.card_game_01.card1)

    def test_game_has_card_02(self):
        self.assertEqual(self.card2, self.card_game_01.card2)


    def test_can_check_for_ace_true(self):
        result = self.card_game_01.check_for_ace(self.card2)
        self.assertEqual(result, True)

    
    def test_can_check_for_ace_false(self):
        result = self.card_game_01.check_for_ace(self.card1)
        self.assertEqual(result, False)


    def test_can_find_highest_card(self):
        result = self.card_game_01.highest_card(self.card1, self.card2)
        self.assertEqual(result, self.card1)

    def test_can_calculate_total(self):
        cards = [self.card1, self.card2]
        result = self.card_game_01.cards_total(cards)
        self.assertEqual(result, 5)
