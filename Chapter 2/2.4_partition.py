#Chapter 2: Linked Lists
#2.4 Partition, page 94
#Partitions a linked list around a value x,
#such that all nodes less than x come before
#all nodes greater than or equal to x.

from LinkedList import LinkedList
import unittest

#Works by rearranging the elements by growing the list at
#the head and tail. Starts a "new" list (using the existing nodes)
#Elements bigger than the pivot are put at the tail and elements 
#smaller are put at the head.
def partition(list, value):
	current = list.tail = list.head

	while current:
		nextNode = current.next
		current.next = None
		if current.data < value:
			current.next = list.head
			list.head = current
		else:
			list.tail.next = current
			list.tail = current
		current = nextNode
		
	#Case that all nodes are less than value
	if list.tail.next:
		list.tail.next = None

#Function to test the partition function. Simply iterates though
#the list until it finds the first value greater than or equal to 
#the pivot value. After that, if a node is found less than the
#pivot, cannot be in the correct order so return false. If we get
#to the end of the list, must be in the correct order so return true.
def checkPartition(list, value):
	current = list.head
	foundPartition = False
	while current:
		if(current.data >= value):
			foundPartition = True
		elif foundPartition:
			return False
		current = current.next
	return True

class Test(unittest.TestCase):
	list1 = LinkedList()
	list1.insert(7)
	list1.insert(6)
	list1.insert(5)
	list1.insert(4)
	list1.insert(3)
	list1.insert(2)
	list1.insert(1)

	testCases = [0, 1, 2, 3, 6, 8]

	def testPartition(self):
		for value in self.testCases:
			partition(self.list1, value)
			self.assertTrue(checkPartition(self.list1, value))

if __name__ == "__main__":
	unittest.main()
