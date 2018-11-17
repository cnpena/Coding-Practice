#Chapter 2: Linked Lists
#2.3 Delete Middle Node, page 94

#Given access to only a node in a linked list, deletes it.
#Works by copying the data from the next node over to the given node
#and then deleting the next node.
from LinkedList import LinkedList
import unittest

def deleteMiddle(node):
	nextNode = node.next
	node.data = nextNode.data
	node.next = nextNode.next

class Test(unittest.TestCase):
	list1 = LinkedList()
	list1.insert(7)
	list1.insert(6)
	list1.insert(5)
	list1.insert(4)
	list1.insert(3)
	list1.insert(2)
	list1.insert(1)

	testCases = [(1, 6), (2,5), (3,4), (4,3), (5,2), (6,1)]

	def testDelete(self):
		for [value, length] in self.testCases:
			node = self.list1.findNode(value)
			deleteMiddle(node)
			self.assertEqual(self.list1.findNode(node), None)
			self.assertEqual(len(self.list1), length)

if __name__ == "__main__":
	unittest.main()
