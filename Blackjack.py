from IPython.display import clear_output
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.takenCards = []

    def build(self):
        clubs = list(range(1,14))
        diamonds = list(range(1,14))
        hearts = list(range(1,14))
        spades = list(range(1,14))
        self.cards = clubs + diamonds + hearts + spades
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

class Dealer(Player):
    def __init__(self):
        self.hand = []
    
class Human(Player):
    def __init__(self):
        self.hand = []
    
class BlackJack():
    def __init__(self):
        self.dealer = Dealer()
        self.human = Human()

    def end(self):
        print(f"The dealer's hand: {self.dealer.hand} = {sum(self.dealer.hand)}")
        print(f"Your hand: {self.human.hand} = {sum(self.human.hand)}")
        if sum(self.dealer.hand) == sum(self.human.hand):
            print('Draw.')
        elif sum(self.dealer.hand) <= sum(self.human.hand) and sum(self.human.hand) <= 21:
            print('You win!')
        else:
            print('You lose!')

    def blackjack(self):
        return "You've gotten a BlackJack, nice!"

    def start(self):
        deck = Deck()
        deck.build()
        deck.shuffle()
        while True:
            start = input("Would you like to start?: ")
            if start.lower() == "no" or start.lower() == "n" or start.lower() == "quit":
                print("Game closed.")
                return
            elif start.lower() == "yes" or start.lower() == "y" or start.lower() == "start" or start.lower() == "hit":
                self.dealer.draw(deck)
                self.dealer.draw(deck)
                print(f"The dealer's hand: [{self.dealer.hand[1]}, X]")
                self.human.draw(deck)
                self.human.draw(deck)
                print(f"Your hand: {(self.human.hand)} = {sum(self.human.hand)}")
                if sum(self.human.hand) == 21:
                    self.blackjack()
                    return
                while True:
                    choice = input("Would you like to hit or stand?: ")
                    if (not choice.isalpha()):
                        print("Please enter a valid response.")
                    else:
                        choice = str(choice)
                        if choice.lower() == 'hit' or choice.lower() == 'h':
                            clear_output(wait=False)
                            self.human.draw(deck)
                            if sum(self.human.hand) == 21:
                                self.end()
                                return
                            elif sum(self.human.hand) >= 21:
                                self.end()
                                return
                            else:
                                print(f"The dealer's hand: [{self.dealer.hand[1]}, X]")
                                print(f"Your hand: {self.human.hand} = {sum(self.human.hand)}")
                                pass
                        elif choice.lower() == 'stand' or choice.lower() == 's':
                            clear_output(wait=False)
                            self.end()
                            return
                        else:
                            print('Please enter a valid response.')
            else:
                print("Please enter a valid response.")


# Blackjack = BlackJack()
# deck = Deck()
# Blackjack.start()
# print(deck.build())
