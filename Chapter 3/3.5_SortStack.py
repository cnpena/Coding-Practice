#Chapter 3: Stacks and Queues
#3.5 Sort Stack, page 99
#Sorts a stack such that the smallest items are on top.
#You can use an additional temporary stack, but you may 
#not copy the elements into any other data structure (such as an array).
#The stack supports the following operations: push, pop, peek, and isEmpty.
#Run time: O(n^2), Space: O(n)
import unittest
from Stack import Stack

def sort(stack):
	sorted = Stack()
	while not stack.isEmpty():
		#insert each element in self in sorted order into sorted
		temp = stack.pop()
		while (not sorted.isEmpty()) and sorted.peek() < temp:
			stack.push(sorted.pop())
		sorted.push(temp)
	return sorted

class Test(unittest.TestCase):

	def test_sort_one_item(self):
		stack = Stack()
		stack.push(1)
		self.assertEqual(stack.peek(), 1)
		sortedStack = sort(stack)
		self.assertEqual(sortedStack.peek(), 1)

	def test_sort_multiple_items(self):
		stack = Stack()
		for i in range(5):
			stack.push(i)
		sortedStack = sort(stack)
		for i in range(5):
			self.assertEqual(sortedStack.pop(), i)

if __name__ == "__main__":
	unittest.main()