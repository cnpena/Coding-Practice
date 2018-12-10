#Chapter 3: Stacks and Queues
#3.6 Animal Shelter, page 99
#Implements an animal shelter based on the following:
#Contains only dogs or cats and operates on a strictly
#first in, first out basis. When people adopt, they can adopt
#the oldest (based on arrival time) or select that they prefer
#a dog or cat (recieve the oldest animal of that type).

#Enqueue, dequeueAny, dequeueDog, dequeuecat

class Node:
	def __init__(self, data, type):
		self.data = data
		self.type = type
		self.next = None

class ShelterList:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, data):
		if self.head is None:
			self.head = self.tail = Node(data)
		else:
			newNode = Node(data)
			self.tail.next = newNode
			self.tail = newNode

	def dequeueAny(self):
		oldest = self.head
		self.head = self.head.next
		return oldest

	def dequeueDog(self):
		current = self.head
		if(current.type is "dog"):
			return current
		else:
			while current:
				if current.type is "dog":
					break
				current = current.next
			return current

	def dequeueCat(self):
		current = self.head
		if(current.type is "cat"):
			return current
		else:
			while current:
				if current.type is "cat":
					break
				current = current.next
			return current