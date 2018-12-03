#Chapter 3: Stacks and Queues
#3.2 Stack Min, page 98
#Implements a stack with a function min which returns the minimum element.
#Push, pop and min all operate in O(1) time.

#Works by noting that the minimum element only changes when a smaller element
#is added or when the smallest element is popped. Simply keeping a minValue 
#variable will break the O(1) constraint since we will have to search through
#the stack to find the new minimum if the minValue is popped from the stack.

#To fix this we will keep an additional stack which keeps track of the minimums
import unittest

class MinStack():

    def __init__(self):
        self.elements = []
        self.minimums = []

    def push(self, item):
        if self.isEmpty():
            self.minimums.append(item)
        else:
            self.minimums.append(min(self.minimums[self.size() - 1], item))
        self.elements.append(item)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        self.minimums.pop()
        return self.elements.pop()

    def minimum(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        return self.minimums[self.size() - 1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.elements)


class Test(unittest.TestCase):

	#If trying to get min from empty stack, exception should be thrown
	def test_min_with_empty_stack(self):
		stack = MinStack()
		with self.assertRaises(Exception) as context:
			stack.minimum()
		self.assertTrue('Stack is empty' in str(context.exception))

	#Min of a stack with a single item should be that single item
	def test_min_with_one_item(self):
		stack = MinStack()
		stack.push(1)
		self.assertEqual(stack.minimum(), 1)

	#If a smaller item is pushed onto the stack, min should change
	def test_push_with_min_change(self):
		stack = MinStack()
		stack.push(1)
		self.assertEqual(stack.minimum(), 1)
		stack.push(0)
		self.assertEqual(stack.minimum(), 0)

	#If a larger item is pushed onto the stack, min shouldn't change
	def test_push_with_min_stays_same(self):
		stack = MinStack()
		stack.push(1)
		self.assertEqual(stack.minimum(), 1)
		stack.push(2)
		self.assertEqual(stack.minimum(), 1)

	#If the current min is popped, the next smallest value should be the new min
	def test_pop_min(self):
		stack = MinStack()
		stack.push(2)
		self.assertEqual(stack.minimum(), 2)
		stack.push(1)
		self.assertEqual(stack.minimum(), 1)
		stack.pop()
		self.assertEqual(stack.minimum(), 2)

	#If a random (non min) value is popped, the min should remain the same
	def test_pop_non_min(self):
		stack = MinStack()
		stack.push(1)
		self.assertEqual(stack.minimum(), 1)
		stack.push(2)
		self.assertEqual(stack.minimum(), 1)
		stack.pop()
		self.assertEqual(stack.minimum(), 1)

if __name__ == "__main__":
	unittest.main()
