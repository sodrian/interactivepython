#!/usr/bin/env python
from random import shuffle


CARD_SUITS = ['s', 'h', 'c', 'd']
CARD_NUMBERS = list(map(str, (range(6, 11)))) + (['j', 'q', 'k', 'a'])


class Card(object):
    def __init__(self, suit, number):
        if suit.lower() not in CARD_SUITS:
            raise ValueError('Not valid card suit')
        if number.lower() not in CARD_NUMBERS:
            raise ValueError('Not valid card number')

        self.suit = suit
        self.number = number
        self.hand = None


class CardContainer(object):
    def __init__(self):
        self.cont = []


class Hand(CardContainer):
    def add(self, cards):
        for c in cards:
            c.hand = self
            self.cont.append(c)

    def withdraw(self, ind):
        return self.cont.pop(ind)


class Deck(CardContainer):
    def __init__(self):
        super(Deck, self).__init__()
        for s in CARD_SUITS:
            for n in CARD_NUMBERS:
                c = Card(s, n)
                self.cont.append(c)
        shuffle(self.cont)

    def pop(self, times):
        l = []
        for t in range(times):
            try:
                c = self.cont.pop()
                l.append(c)
            except IndexError:
                break
        return l


class Table(CardContainer):
    def go_with(self, card):
        self.cont.append(card)


if __name__ == '__main__':
    d = Deck()
    h1 = Hand()
    h2 = Hand()

    h1.add(d.pop(6))
    h2.add(d.pop(6))

    t = Table()

    print(t)
    print(h1)
    print(h2)
