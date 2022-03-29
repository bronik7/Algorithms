from Card import Card
from random import shuffle


class Deck:
    number_of_cards = 52

    def __init__(self):
        suite = ("Hearts", "Diamonds", "Clubs", "Spades")
        value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = []
        for k in suite:
            for v in value:
                self.cards.append(Card(k, v))
        self.number = len(self.cards)

    def count(self):
        return Deck.number_of_cards

    def __repr__(self):
        return f"Deck of {Deck.number_of_cards}  cards"

    def _deal(self, number):
        if number > len(self.cards):
            raise ValueError("All cards have been dealt")
        cards = self.cards[len(self.cards) - number:]
        del self.cards[len(self.cards) - number:]
        Deck.number_of_cards -= number
        return cards

    def shuffle(self):
        if len(self.cards) < 52:
            return
        shuffle(self.cards)

    def deal_card(self):

        return self.cards.pop()

    def deal_hand(self, number):
        return self._deal(number)


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(53)
print(hand)
print(my_deck.count())
my_deck.shuffle()
