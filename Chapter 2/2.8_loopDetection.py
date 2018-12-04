#Chapter 2: Linked Lists
#2.8 Loop Detection, page 95
#Given a circular linked list, returns the node at the beginning of the loop.
#Example: Input: A -> B -> C -> D -> E -> C (The same C as earlier)
#Output: C

from LinkedList import LinkedList
import unittest

#Works by using two pointers, fast and slow. Fast pointer moves at 2x the speed
#of slow pointer. When they collide, move slow to head. Fast stays where it is.
#Move both pointers at a rate of 1 step until they reach the collision point
#(start of the loop)
def isLoop(list):
	fast = slow = list.head

	#find meeting point, this will be loopSize-k steps into the linked list
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if(slow is fast):
			break

	#Error check: no meeting point - therefore no loop
	if not fast or not fast.next:
		return None

	#Move slow to head. Keep fast at meeting point. Each are k steps from the
	#loop start. Since they move at the same pace, they must meet at the loop 
	#start.
	slow = list.head
	while slow is not fast:
		slow = slow.next
		fast = fast.next

	return fast.data

class Test(unittest.TestCase):

	#A single element should not be counted as a loop
	def test_loop_single_element(self):
		list = LinkedList()
		list.insert('a')
		self.assertEqual(isLoop(list), None)

	def test_loop_true(self):
		list = LinkedList()
		list.insert('d')
		list.insert('c')
		list.insert('b')
		list.insert('a')
		list.tail.next = list.head
		self.assertEqual(isLoop(list), 'a')

	def test_loop_false(self):
		list = LinkedList()

		list.insert('a')
		list.insert('b')
		list.insert('a')
		self.assertEqual(isLoop(list), None)

if __name__ == "__main__":
	unittest.main()