import unittest
from Blackjack import Deck, Player, Dealer, Human, BlackJack

class TestBlackJack(unittest.TestCase):

    def testDeck(self):
        testDeck = Deck()
        self.assertEqual(testDeck.cards, [])
        self.assertEqual(testDeck.build(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(testDeck.takenCards, [])

    def testBlackJack(self):
        testBlackJack = BlackJack()
        self.assertEqual(testBlackJack.blackjack(), "You've gotten a BlackJack, nice!")
    
    
if __name__ == '__main__':
    unittest.main()
