#Chapter 2: Linked Lists
#2.1 Remove Dups, page 94
#Removes duplicates from an unsorted linked list

#Utilize hash table to save values, when we come across a
#value that already exists in the linked list, remove it 
#As we iterate, keeps a reference to the node prev to the
#current node for easy deletion.
#Run time: O(n)
from LinkedList import LinkedList
import unittest

def removeDuplicates(list):
 	table = {}
 	current = list.head
 	prev = None

 	while(current):
 		if(current.data not in table):
 			table[current.data] = 1
 			prev = current
 		else:
 			prev.next = current.next
 		current = current.next
 	return list.asList()

#Alternate method, O(n^2) run time but O(1) space
#Iterates with two pointers, current which iterates through
#the linked list and runner which checks all subsequent nodes 
#for duplicates, removing any duplicates it finds.
def removeDuplicates2(list):
 	current = list.head
 	while(current):
 		runner = current
 		while(runner.next):
 			if(runner.next.data == current.data):
 				runner.next = runner.next.next
 			else:
 				runner = runner.next
 		current = current.next
 	return list.asList()

class Test(unittest.TestCase):
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(3)

    list2 = LinkedList()
    list2.insert(1)
    list2.insert(2)
    list2.insert(3)

    output = [3, 2, 1]


    data = [(list1, output),
            (list2, output)]

    def testForDuplicates(self):
        for [list, expected] in self.data:
            self.assertEqual(removeDuplicates(list), expected)
            self.assertEqual(removeDuplicates2(list), expected)

if __name__ == "__main__":
    unittest.main()

