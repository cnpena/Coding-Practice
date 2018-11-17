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
    list1 = LinkedList()
    list2 = LinkedList()

    list1.insert('d')
    list1.insert('c')
    list1.insert('b')
    list1.insert('a')
    list1.tail.next = list1.head

    list2.insert('a')
    list2.insert('b')
    list2.insert('a')

    def testSum(self):
    	self.assertEqual(isLoop(self.list1), 'a')
    	self.assertEqual(isLoop(self.list2), None)

if __name__ == "__main__":
    unittest.main()