#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import random

class Deck(object):
    base_deck = [u'A♠',u'2♠',u'3♠',u'4♠',u'5♠',u'6♠',u'7♠',u'8♠',u'9♠',u'J♠',u'Q♠',u'K♠',
                 u'A♣',u'2♣',u'3♣',u'4♣',u'5♣',u'6♣',u'7♣',u'8♣',u'9♣',u'J♣',u'Q♣',u'K♣',
                 u'A♥',u'2♥',u'3♥',u'4♥',u'5♥',u'6♥',u'7♥',u'8♥',u'9♥',u'J♥',u'Q♥',u'K♥',
                 u'A♦',u'2♦',u'3♦',u'4♦',u'5♦',u'6♦',u'7♦',u'8♦',u'9♦',u'J♦',u'Q♦',u'K♦'
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

    def deal_pretty(self,h=''):
        if h == '':
            h = self.deal()
        hand = u'',h[0],' ',h[1],' ',h[2],' ',h[3],' ',h[4]
        hand.replace("♥","[color=red]♥[/color]")
        hand.replace("♦","[color=red]♦[/color]")
        return hand

if __name__ == "__main__":
    print "Hello World"
    d = Deck()
    hand = d.deal()

    print u'Cards: ',hand[0],' ',hand[1],' ',hand[2],' ',hand[3],' ',hand[4]
    print u'Pretty: ',d.deal_pretty(hand)