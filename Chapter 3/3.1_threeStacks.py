#Chapter 3: Stacks and Queues
#3.1 Three in One, page 98
#Uses a single array to implement 3 stacks
#Works by dividing the array in three equal parts 
#and allowing the individual stack to grow in that limited space. 
#Note: If we had additional information about the expected usages 
#of the stacks, then we could modify this algo­rithm accordingly.
import unittest

class FixedMultiStack:

	def __init__(self, stackSize):
		self.numberOfStacks = 3
		self.stackSize 		= stackSize
		self.values 		= [0] * (stackSize * self.numberOfStacks)
		self.sizes 			= [0] * self.numberOfStacks

	#Push value onto stack
	def push(self, stackNum, value):
		#Check that we have enough space to add new element
		if self.isFull(stackNum):
			raise Exception('Stack is full')
		#Increment stack pointer and update top value
		self.sizes[stackNum] += 1
		topIndex = self.topIndex(stackNum)
		self.values[topIndex] = value

	#Pop element from top of stack, return element
	def pop(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception('Stack is empty')

		topIndex = self.topIndex(stackNum)
		value = self.values[topIndex]
		self.values[topIndex] = 0
		self.sizes[stackNum] -= 1
		return value

	#Return top element
	def peek(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception('Stack is empty')

		topIndex = self.topIndex(stackNum)
		value = self.values[topIndex]
		return value

	#Return if stack is full
	def isFull(self, stackNum):
		return self.sizes[stackNum] == self.stackSize

	#Return if stack is empty
	def isEmpty(self, stackNum):
		return self.sizes[stackNum] == 0

	#Returns index of the top of the stack
	def topIndex(self, stackNum):
		offset = stackNum * self.stackSize
		size = self.sizes[stackNum]
		return offset + size - 1

class Test(unittest.TestCase):

	#Stacks should be empty when created
	def test_empty_stack_when_created(self):
		stack = FixedMultiStack(4)
		self.assertTrue(stack.isEmpty(0))
		self.assertTrue(stack.isEmpty(1))
		self.assertTrue(stack.isEmpty(2))

	#Push value to each stack, stacks should no longer be empty
	def test_non_empty_stack_after_push(self):
		stack = FixedMultiStack(4)
		for value in range(2):
			self.pushToEachStack(stack, value)
			self.assertFalse(stack.isEmpty(0))
			self.assertFalse(stack.isEmpty(1))
			self.assertFalse(stack.isEmpty(2))

	#Push value to stack, pop value from stack. Stack should be empty
	def test_empty_stack_after_pop(self):
		stack = FixedMultiStack(4)
		self.pushToEachStack(stack, 1)
		stack.pop(0)
		self.assertTrue(stack.isEmpty(0))

	#Push value to each stack, test peek function
	def test_peek_values(self):
		stack = FixedMultiStack(4)
		for value in range(3):
			self.pushToEachStack(stack, value)
			self.assertEqual(stack.peek(0), value)
			self.assertEqual(stack.peek(1), value)
			self.assertEqual(stack.peek(2), value)

	#Push 3 values to each stack, pop & check values
	def test_pop_values(self):
		stack = FixedMultiStack(4)
		for value in range(3):
			self.pushToEachStack(stack, value)
		for value in range(2, 0, -1):
			self.assertEqual(stack.pop(0), value)
			self.assertEqual(stack.pop(1), value)
			self.assertEqual(stack.pop(2), value)

	#Push values to each stack, test stack is not full
	def test_stack_is_not_full(self):
		stack = FixedMultiStack(4)
		for value in range(3):
			self.pushToEachStack(stack, value)
			self.assertFalse(stack.isFull(0))
			self.assertFalse(stack.isFull(1))
			self.assertFalse(stack.isFull(2))

	#Push values to each stack, test stack is full
	def test_stack_is_full(self):
		stack = FixedMultiStack(4)
		for value in range(4):
			self.pushToEachStack(stack, value)
		self.assertTrue(stack.isFull(0))
		self.assertTrue(stack.isFull(1))
		self.assertTrue(stack.isFull(2))

	#Push to full stack, expects a 'Stack is full' exception
	def test_push_to_full_stack(self):
		stack = FixedMultiStack(1)
		self.pushToEachStack(stack, 1)
		with self.assertRaises(Exception) as context:
			stack.push(0, 1)
		self.assertTrue('Stack is full' in str(context.exception))

	#Pop from empty stack, expects a 'Stack is empty' exception
	def test_pop_from_empty_stack(self):
		stack = FixedMultiStack(1)
		with self.assertRaises(Exception) as context:
			stack.pop(1)
		self.assertTrue('Stack is empty' in str(context.exception))

	#Peek from empty stack, expects a 'Stack is empty' exception
	def test_peek_from_empty_stack(self):
		stack = FixedMultiStack(1)
		with self.assertRaises(Exception) as context:
			stack.peek(1)
		self.assertTrue('Stack is empty' in str(context.exception))

	#Pushes a value to each stack
	def pushToEachStack(self, stack, value):
		stack.push(0, value)
		stack.push(1, value)
		stack.push(2, value)

if __name__ == "__main__":
	unittest.main()
