#Chapter 3: Stacks and Queues
#3.5 Sort Stack, page 99
#Sorts a stack such that the smallest items are on top.
#You can use an additional temporary stack, but you may 
#not copy the elements into any other data structure (such as an array).
#The stack supports the following operations: push, pop, peek, and isEmpty.

class SortStack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]