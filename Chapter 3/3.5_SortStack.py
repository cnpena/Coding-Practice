#Chapter 3: Stacks and Queues
#3.5 Sort Stack, page 99
#Sorts a stack such that the smallest items are on top.
#You can use an additional temporary stack, but you may 
#not copy the elements into any other data structure (such as an array).
#The stack supports the following operations: push, pop, peek, and isEmpty.
#Run time: O(n^2), Space: O(n)
import unittest

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

	def sort(self):
		stack2 = SortStack()
		while not self.isEmpty():
			#insert each element in self in sorted order into stack2
			temp = self.pop()
			while not stack2.isEmpty and stack2.peek() > temp:
				self.push(stack2.pop())
			stack2.push(temp)

		#copy elements from stack2 back into self
		while not stack2.isEmpty():
			self.push(stack2.pop())

class Test(unittest.TestCase):

	def test_sort_one_item(self):

	def test_sort_multiple_items(self):

if __name__ == "__main__":
	unittest.main()