#!/usr/bin/python
import random

class Deck(object):
    base_deck = ['A♠','1♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','J♠','Q♠','K♠',
                 'A♣','1♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','J♣','Q♣','K♣',
                 'A♥','1♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','J♥','Q♥','K♥',
                 'A♦','1♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','J♦','Q♦','K♦'
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
