#Alternate solution to 3.6 Animal Shelter. This solution separates
#the animal shelter list into a list of dogs and a list of cats.
#Prevents from having to iterate through the list when dequeueCat
#or dequeueDog is called.
from collections import deque
import unittest

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = -1

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

class ShelterList(object):
    
    def __init__(self):
        self.Dog = deque()
        self.Cat = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1 
        if isinstance(animal, Cat):
            self.Cat.append(animal)
        else:
            self.Dog.append(animal)

    def dequeueAny(self):
        if len(self.Dog) == 0:
            return self.dequeueCat()
        if len(self.Cat) == 0:
            return self.dequeueDog()
        if self.Dog[0].order < self.Cat[0].order:
            return self.Dog.popleft()
        else:
            return self.Cat.popleft()

    def dequeueDog(self):
    	if len(self.Dog) != 0:
    		return self.Dog.popleft()
    	else:
    		return None

    def dequeueCat(self):
    	if len(self.Cat) != 0:
    		return self.Cat.popleft()
    	else:
    		return None

class Test(unittest.TestCase):

	#Simple test to ensure that enqueue 1 dog works
	def test_enqueue_one_dog(self):
		list = ShelterList()
		list.enqueue(Dog("dog1"))
		self.assertEqual(list.dequeueDog().name, "dog1")

	#Simple test to ensure that enqueue 1 cat works
	def test_enqueue_one_cat(self):
		list = ShelterList()
		list.enqueue(Cat("cat1"))
		self.assertEqual(list.dequeueCat().name, "cat1")

	#Test that dequeueDog properly returns the oldest dog in a list
	#of only dogs
	def test_dequeue_dogs(self):
		list = ShelterList()
		list.enqueue(Dog("dog1"))
		list.enqueue(Dog("dog2"))
		list.enqueue(Dog("dog3"))
		self.assertEqual(list.dequeueDog().name, "dog1")
		self.assertEqual(list.dequeueDog().name, "dog2")
		self.assertEqual(list.dequeueDog().name, "dog3")

	#Test that dequeueCat properly returns the oldest cat in a list
	#of only cats
	def test_dequeue_cats(self):
		list = ShelterList()
		list.enqueue(Cat("cat1"))
		list.enqueue(Cat("cat2"))
		list.enqueue(Cat("cat3"))
		self.assertEqual(list.dequeueCat().name, "cat1")
		self.assertEqual(list.dequeueCat().name, "cat2")
		self.assertEqual(list.dequeueCat().name, "cat3")

	#Test that dequeue properly returns the oldest animal in a list
	#of both cats and dogs
	def test_dequeue_any(self):
		list = ShelterList()
		list.enqueue(Cat("cat1"))
		list.enqueue(Dog("dog1"))
		self.assertEqual(list.dequeueAny().name, "cat1")
		self.assertEqual(list.dequeueAny().name, "dog1")

	#Test that dequeueDog properly returns the oldest dog in a list
	#of both cats and dogs
	def test_dequeue_dog2(self):
		list = ShelterList()
		list.enqueue(Cat("cat1"))
		list.enqueue(Dog("dog1"))
		list.enqueue(Dog("dog2"))
		self.assertEqual(list.dequeueDog().name, "dog1")

	#Test that dequeueCat properly returns the oldest cat in a list
	#of both cats and dogs
	def test_dequeue_cat2(self):
		list = ShelterList()
		list.enqueue(Dog("dog1"))
		list.enqueue(Cat("cat1"))
		list.enqueue(Cat("cat2"))
		self.assertEqual(list.dequeueCat().name, "cat1")

if __name__ == "__main__":
	unittest.main()