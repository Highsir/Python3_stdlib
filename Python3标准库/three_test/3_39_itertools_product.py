from itertools import *
import pprint

face_cards = ('J','Q','K','A')
suits = ('H','D','C','S')

deck = list(
    product(
        chain(range(2,11),face_cards),
        suits
    )
)
print(deck)

for card in deck:
    print('{:>2}{}'.format(*card),end=' ')
    if card[1] == suits[-1]:
        print()