#Chapter 3: Stacks and Queues
#3.4 Queue via Stacks, page 99
#Implements a queue using two stacks, newest (newest elements on top)
#and oldest (oldest elements on top). When an element is dequeued,
#dequeues from oldest since a queue removes the oldest element first.
#To insert an element, push onto the newest stack since it has the 
#newest elements on top.
from Stack import Stack
import unittest

class StackQueue:

	def __init__(self):
		self.newest = Stack()
		self.oldest = Stack()

	def size(self):
		return self.newest.size() + self.oldest.size()

	def push(self, value):
		self.newest.push(value)

	#Move elements from newest into oldest. 
	#Used when we want to peek or pop from queue. 
	def shiftNewToOld(self):
		if self.oldest.isEmpty():
			while not self.newest.isEmpty():
				self.oldest.push(self.newest.pop())

	#Shifts all elements from newest to oldest, so oldest
	#element is at top of oldest stack. Then, peek at top
	#of oldest stack
	def peek(self):
		self.shiftNewToOld()
		return self.oldest.peek()

	#Shifts all elements from newest to oldest, so oldest
	#element is at top of oldest stack. Then, pop from top
	#of oldest stack.
	def pop(self):
		self.shiftNewToOld()
		return self.oldest.pop()


class Test(unittest.TestCase):

	#Verify size function is working as expected.
	#All values should be pushed to 'newest' stack
	def test_size(self):
		queue = StackQueue()
		for i in range(1, 10):
			queue.push(i)
		self.assertEqual(queue.size(), i)
		self.assertEqual(queue.newest.size(), i)

	#Verify that size is decreased when pop is called
	def test_size_after_pop(self):
		queue = StackQueue()
		queue.push(1)
		self.assertEqual(queue.size(), 1)
		queue.pop()
		self.assertEqual(queue.size(), 0)

	#Verify that size is not changed when peek is called
	def test_size_after_peek(self):
		queue = StackQueue()
		queue.push(1)
		self.assertEqual(queue.size(), 1)
		queue.peek()
		self.assertEqual(queue.size(), 1)

	#Verify value using peek with a single element.
	def test_peek_single_element(self):
		queue = StackQueue()
		queue.push(1)
		self.assertEqual(queue.peek(), 1)

	#Verify that peek returns the first element pushed
	def test_peek_multiple_elements(self):
		queue = StackQueue()
		for i in range(3):
			queue.push(i)
		self.assertEqual(queue.peek(), 0)

	#Verify value using pop with a single element
	def test_pop_single_element(self):
	 	queue = StackQueue()
	 	queue.push(1)
	 	self.assertEqual(queue.pop(), 1)

	#Verify value using pop with multiple elements
	def test_pop_multiple_elements(self):
		queue = StackQueue()
		for i in range(0, 10):
			queue.push(i)
		for i in range(0, 10):
			self.assertEqual(queue.pop(), i)

if __name__ == "__main__":
	unittest.main()