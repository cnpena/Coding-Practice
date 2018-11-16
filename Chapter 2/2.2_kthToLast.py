#Chapter 2: Linked Lists
#2.2 Return Kth to Last
#Returns the kth to last element of a singly linked list
from LinkedList import LinkedList
import unittest

 #recursive: Recurses through the linked list, counting the
 #number of nodes from the end. When it hits the end, returns 0.
 #Run time: O(n), Space: O(n)
def findKth(current, index):
	if(current is None):
		return(0)

	i = findKth(current.next, index)+1
	if(i == index):
		print(str(index), 'th node is ', current.data)
	return i

#Iterative: Uses two pointers to move through the linked list.
#They are placed k nodes apart and move at the same pace. When
#pointer1 hits the end, pointer2 will be k nodes from the end (as desired)
#Run time: O(n), Space: O(1)
def findKth2(head, k):
	pointer1 = head
	pointer2 = head
	for i in range(k):
		pointer1 = pointer1.next
	while(pointer1 is not None):
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	return pointer2.data


class Test(unittest.TestCase):
    list1 = LinkedList()
    list1.insert(7)
    list1.insert(6)
    list1.insert(5)
    list1.insert(4)
    list1.insert(3)
    list1.insert(2)
    list1.insert(1)

    testCases = [(1, 7), (2,6), (3,5), (4,4), (5,3), (6,2), (7,1)]

    def testKth(self):
        for [k, expected] in self.testCases:
            self.assertEqual(findKth2(self.list1.head, k), expected)

if __name__ == "__main__":
    unittest.main()