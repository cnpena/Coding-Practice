#Chapter 3: Stacks and Queues
#3.6 Animal Shelter, page 99
#Implements an animal shelter based on the following:
#Contains only dogs or cats and operates on a strictly
#first in, first out basis. When people adopt, they can adopt
#the oldest (based on arrival time) or select that they prefer
#a dog or cat (recieve the oldest animal of that type).

#Enqueue, dequeueAny, dequeueDog, dequeuecat
import unittest

class Animal:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.next = None

class ShelterList:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, name, type):
		if self.head is None:
			self.head = self.tail = Animal(name, type)
		else:
			newNode = Animal(name, type)
			self.tail.next = newNode
			self.tail = newNode

	def dequeueAny(self):
		oldest = self.head
		self.head = self.head.next
		return oldest

	def dequeueDog(self):
		current = self.head
		if(current.type is "dog"):
			self.head = current.next
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
			self.head = current.next
			return current
		else:
			while current:
				if current.type is "cat":
					break
				current = current.next
			return current

class Test(unittest.TestCase):

	#Simple test to ensure that enqueue sets both head and tail properly
	def test_enqueue_one_dog(self):
		list = ShelterList()
		list.enqueue("dog1", "dog")
		self.assertEqual(list.head.name, "dog1")
		self.assertEqual(list.tail.name, "dog1")

	#Simple test to ensure that enqueue sets both head and tail properly
	def test_enqueue_one_cat(self):
		list = ShelterList()
		list.enqueue("cat1", "cat")
		self.assertEqual(list.head.name, "cat1")
		self.assertEqual(list.tail.name, "cat1")

	#Test that dequeue dog with 1 dog works
	def test_dequeue_one_dog(self):
		list = ShelterList()
		list.enqueue("dog1", "dog")
		oldestDog = list.dequeueDog()
		self.assertEqual(oldestDog.name, "dog1")

	#Test that dequeue dog with 1 cat works
	def test_dequeue_one_cat(self):
		list = ShelterList()
		list.enqueue("cat1", "cat")
		oldestCat = list.dequeueCat()
		self.assertEqual(oldestCat.name, "cat1")

	#Test that dequeueDog properly returns the oldest dog in a list
	#of only dogs
	def test_dequeue_dogs(self):
		list = ShelterList()
		list.enqueue("dog1", "dog")
		list.enqueue("dog2", "dog")
		list.enqueue("dog3", "dog")
		self.assertEqual(list.dequeueDog().name, "dog1")
		self.assertEqual(list.dequeueDog().name, "dog2")
		self.assertEqual(list.dequeueDog().name, "dog3")

	#Test that dequeueCat properly returns the oldest cat in a list
	#of only cats
	def test_dequeue_cats(self):
		list = ShelterList()
		list.enqueue("cat1", "cat")
		list.enqueue("cat2", "cat")
		list.enqueue("cat3", "cat")
		self.assertEqual(list.dequeueCat().name, "cat1")
		self.assertEqual(list.dequeueCat().name, "cat2")
		self.assertEqual(list.dequeueCat().name, "cat3")

	#Test that dequeue properly returns the oldest animal in a list
	#of both cats and dogs
	def test_dequeue_any(self):
		list = ShelterList()
		list.enqueue("cat1", "cat")
		list.enqueue("dog1", "dog")
		self.assertEqual(list.dequeueAny().name, "cat1")
		self.assertEqual(list.dequeueAny().name, "dog1")

	#Test that dequeueDog properly returns the oldest dog in a list
	#of both cats and dogs
	def test_dequeue_dog2(self):
		list = ShelterList()
		list.enqueue("cat1", "cat")
		list.enqueue("dog1", "dog")
		list.enqueue("dog2", "dog")
		self.assertEqual(list.dequeueDog().name, "dog1")

	#Test that dequeueCat properly returns the oldest cat in a list
	#of both cats and dogs
	def test_dequeue_cat2(self):
		list = ShelterList()
		list.enqueue("dog1", "dog")
		list.enqueue("cat1", "cat")
		list.enqueue("cat2", "cat")
		self.assertEqual(list.dequeueCat().name, "cat1")

if __name__ == "__main__":
	unittest.main()