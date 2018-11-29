#Chapter 3: Stacks and Queues
#3.2 Stack Min, page 98
#Implements a stack with a function min which returns the minimum element.
#Push, pop and min all operate in O(1) time.

#Works by noting that the minimum element only changes when a smaller element
#is added or when the smallest element is popped. Simply keeping a minValue 
#variable will break the O(1) constraint since we will have to search through
#the stack to find the new minimum if the minValue is popped from the stack.

#To fix this we will keep an additional stack which keeps track of the minimums

class Stack():

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


stack = Stack()
stack.push(3)
print(stack.minimum())
stack.push(5)
print(stack.minimum())
stack.push(1)
print(stack.minimum())
stack.pop()
print(stack.minimum())