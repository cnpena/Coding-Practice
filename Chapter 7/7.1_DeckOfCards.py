#Chapter 7: Object-Oriented Design
#7.1 Deck of Cards, page 125
#Data structure for a generic deck of cards

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

class Deck:
	def __init__(self, )