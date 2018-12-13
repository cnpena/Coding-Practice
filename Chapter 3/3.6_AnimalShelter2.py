#Alternate solution to 3.6 Animal Shelter. This solution separates
#the animal shelter list into a list of dogs and a list of cats.
#Prevents from having to iterate through the list when dequeueCat
#or dequeueDog is called.

class Animal:
	def __init__(self, name, time):
		self.name = name
		self.time = time
		self.next = None

	def isOlderThan(self, animal2):
		return self.time > animal2.time

class ShelterList:

	def __init__(self, type):
		self.head = None
		self.tail = None

	def enqueue(self, name, type):
		if self.head is None:
			self.head = self.tail = Animal(name, type, time)
		else:
			newNode = Animal(name, type, time)
			self.tail.next = newNode
			self.tail = newNode

	def dequeueAny(self):

		oldest = self.head
		self.head = self.head.next
		return oldest

	# def dequeueDog(self):
	# 	current = self.head
	# 	if(current.type is "dog"):
	# 		self.head = current.next
	# 		return current
	# 	else:
	# 		while current:
	# 			if current.type is "dog":
	# 				break
	# 			current = current.next
	# 		return current

	# def dequeueCat(self):
	# 	current = self.head
	# 	if(current.type is "cat"):
	# 		self.head = current.next
	# 		return current
	# 	else:
	# 		while current:
	# 			if current.type is "cat":
	# 				break
	# 			current = current.next
	# 		return current
