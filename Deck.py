#!/usr/bin/python
import random

class Deck(object):
    base_deck = [
                 u'A\u2660',u'1\u2660',u'2\u2660',u'3\u2660',u'4\u2660',
                 u'5\u2660',u'6\u2660',u'7\u2660',u'8\u2660',u'9\u2660',
                 u'J\u2660',u'Q\u2660',u'K\u2660',
                 
                 u'A\u2665',u'1\u2665',u'2\u2665',u'3\u2665',u'4\u2665',
                 u'5\u2665',u'6\u2665',u'7\u2665',u'8\u2665',u'9\u2665',
                 u'J\u2665',u'Q\u2665',u'K\u2665',

                 u'A\u2666',u'1\u2666',u'2\u2666',u'3\u2666',u'4\u2666',
                 u'5\u2666',u'6\u2666',u'7\u2666',u'8\u2666',u'9\u2666',
                 u'J\u2666',u'Q\u2666',u'K\u2666',

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
    hand = d.deal()

    print u'Cards: ',hand[0],' ',hand[1],' ',hand[2],' ',hand[3],' ',hand[4]
