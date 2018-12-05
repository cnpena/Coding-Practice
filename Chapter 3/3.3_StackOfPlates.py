#Chapter 3: Stacks and Queues
#3.3 Stack of Plates, page 99
#Implements a data structure that is composed of several stacks.
#Creates a new stack once the previous one exceeds capacity.
import unittest

class SetOfStacks:

	def __init__(self, capacity):
		self.stacks = []
		self.capacity = capacity

	#Pushes value to a substack. If this is the first element or the capacity
	#has been reached, a new substack is added. Then, appends to the last
	#stack in the set.
	def push(self, value):
		if(len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity):
			self.stacks.append([])
		self.stacks[-1].append(value)

	#Pops from the last stack in the set and returns the value. Throws an 
	#exception if it is completely empty. If we have popped the only value
	#in a substack, pops that stack from the set.
	def pop(self):
		if(len(self.stacks) == 0):
			raise ValueError('Stack is empty')
		node = self.stacks[-1].pop()
		if len(self.stacks[-1]) == 0:
			self.stacks.pop()
		return node

	#Pops from top of stack at index and returns the value. Throws an
	#exception if the index does not exist as a substack. Note: This does
	#allow for substacks to potentially not be filled anymore.
	def popAt(self, index):
		if index < 1 or index > len(self.stacks):
			raise ValueError('Invalid Index')

		node = self.stacks[index-1].pop()
		if(len(self.stacks[index-1]) == 0):
			self.stacks.remove([])

		return node

class Test(unittest.TestCase):

	#Popping from empty stack should throw exception
	def test_pop_from_empty_stack(self):
		stack = SetOfStacks(3)
		with self.assertRaises(Exception) as context:
			stack.pop()
		self.assertTrue('Stack is empty' in str(context.exception))

	#If capacity is reached, a new stack should be added
	def test_add_new_stack(self):
		stack = SetOfStacks(1)
		stack.push(1)
		self.assertEqual(len(stack.stacks), 1)
		stack.push(2)
		self.assertEqual(len(stack.stacks), 2)
		stack.push(3)
		self.assertEqual(len(stack.stacks), 3)

	#If all elements are popped from a substack, should be removed from list
	def test_remove_stack_if_empty(self):
		stack = SetOfStacks(1)
		stack.push(1)
		self.assertEqual(len(stack.stacks), 1)
		stack.pop()
		self.assertEqual(len(stack.stacks), 0)

	#Verify the correct values are popped from a single substack
	def test_pop_correct_value_single_substack(self):
		stack = SetOfStacks(2)
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.pop(), 1)

	#Verify the correct values are popped from multiple substacks
	def test_pop_correct_value_multiple_substacks(self):
		stack = SetOfStacks(1)
		stack.push(1)
		stack.push(2)
		stack.push(3)
		self.assertEqual(stack.pop(), 3)
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.pop(), 1)

	#Should throw an error if trying to pop from non-existent substack
	def test_popAt_invalid_index(self):
		stack = SetOfStacks(1)
		with self.assertRaises(Exception) as context:
			stack.popAt(0)
		self.assertTrue('Invalid Index' in str(context.exception))
		with self.assertRaises(Exception) as context:
			stack.popAt(5)
		self.assertTrue('Invalid Index' in str(context.exception))

	#Verify the correct values are popped from a single substack
	def test_popAt_single_substack(self):
		stack = SetOfStacks(2)
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.popAt(1), 2)
		self.assertEqual(stack.popAt(1), 1)

	#Verify the correct values are popped from multiple substacks
	def test_popAt_multiple_substacks(self):
		stack = SetOfStacks(1)
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.popAt(2), 2)
		self.assertEqual(stack.popAt(1), 1)

if __name__ == "__main__":
	unittest.main()