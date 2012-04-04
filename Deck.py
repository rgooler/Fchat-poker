#!/usr/bin/python
import random

class Deck(object):
    base_deck = [
                 u'A\u2660',u'1\u2660',u'2\u2660',u'3\u2660',u'4\u2660',
                 u'5\u2660',u'6\u2660',u'7\u2660',u'8\u2660',u'9\u2660',
                 u'J\u2660',u'Q\u2660',u'K\u2660',
                 
                 u'A\u2661',u'1\u2661',u'2\u2661',u'3\u2661',u'4\u2661',
                 u'5\u2661',u'6\u2661',u'7\u2661',u'8\u2661',u'9\u2661',
                 u'J\u2661',u'Q\u2661',u'K\u2661',

                 u'A\u2662',u'1\u2662',u'2\u2662',u'3\u2662',u'4\u2662',
                 u'5\u2662',u'6\u2662',u'7\u2662',u'8\u2662',u'9\u2662',
                 u'J\u2662',u'Q\u2662',u'K\u2662',

                 u'A\u2663',u'1\u2663',u'2\u2663',u'3\u2663',u'4\u2663',
                 u'5\u2663',u'6\u2663',u'7\u2663',u'8\u2663',u'9\u2663',
                 u'J\u2663',u'Q\u2663',u'K\u2663'
                ]

    deck = []
    decks = 1
    cards_used = 0

    def __init__(self,decks=1,debug=False):
        self.set_decks(decks)

    def set_decks(self,decks):
        self.decks = decks
        self.deck = []
        while decks:
            decks = decks - 1
            self.deck += self.base_deck
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        new_cards_used = self.cards_used + 5
        hand = self.deck[self.cards_used:new_cards_used]
        if len(self.deck) - new_cards_used <= 10:
            self.shuffle()
            self.cards_used = 0
        else:
            self.cards_used = new_cards_used

        return hand

if __name__ == "__main__":
    print "Hello World"
    d = Deck()
    print d.deal()
