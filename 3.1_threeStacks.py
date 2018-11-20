#Chapter 3: Stacks and Queues
#3.1 Three in One, page 98
#Uses a single array to implement 3 stacks
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
		return offset + self.sizes[stackNum] - 1


newstack = FixedMultiStack(2)
print(newstack.isEmpty(1))
newstack.push(1,3)
print (newstack.peek(1))
print (newstack.isEmpty(1))
newstack.push(1,2)
print (newstack.peek(1))
print (newstack.pop(1))
print (newstack.peek(1))
newstack.push(1,3)