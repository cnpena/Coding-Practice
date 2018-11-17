#Chapter 2: Linked Lists
#2.6 Palindrome, page 95
#Checks whether a linked list is a palindrome

#Reverses the linked list and compares the original to the reversed
#If they are the same, the list must be a palindrome.
from LinkedList import LinkedList
import unittest

def isPalindrome(list):
	reversed = reverseList(list.head)
	return isEqual(list.head, reversed.head)
		
#Simply reverses a list by iterating through the original and copying
#to a new list. By using insert, copies in reverse order.
def reverseList(node):
	list = LinkedList()
	while node:
		list.insert(node.data)
		node = node.next
	return list

#Determines if the two lists are equal by iterating through them both.
#If a node is reached in which the two lists are not equal, cannot be a
#palindrome so return false. Otherwise, if we've gotten to the end of both
#lists, must be equivalent.
def isEqual(list1, list2):
	while list1 and list2:
		if list1.data is not list2.data:
			return False
		list1 = list1.next
		list2 = list2.next
	return list1 is None and list2 is None

#Iterative approach: (assumes we don't know the length of the list)
#Using a fast and slow runner, iterate through the linked list. 
#At each iteration, push the data from the slow runner onto the stack.
#Since the fast runner moves at 2x the speed, when the fast runner hits the
#end of the list, the slow runner will be in the middle.
#Then, pop from the stack and compare against the data in the latter half
#of the linked list, returning true only if they all match.
def isPalindrome2(list):
	fast = list.head
	slow = list.head

	stack = []
	while fast and fast.next:
		stack.append(slow.data)
		slow = slow.next
		fast = fast.next.next

	if(fast): #odd length list
		slow = slow.next

	while slow:
		top = stack.pop()
		if top is not slow.data:
			return False
		slow = slow.next
	return True

class Test(unittest.TestCase):
    str1 = LinkedList()
    str2 = LinkedList()
    str3 = LinkedList()
    str4 = LinkedList()

    str1.insert('a')
    str1.insert('b')
    str1.insert('a')

    str2.insert('a')
    str2.insert('a')

    str3.insert('a')
    str3.insert('b')
    str3.insert('c')

    str4.insert('a')
    str4.insert('b')

    sol1 = [4, 3, 2, 1]
    sol2 = [0, 4, 6]

    palindromes = [str1, str2]

    notPalindromes = [str3]#, str4]

    def testSum(self):
        for string in self.palindromes:
            self.assertTrue(isPalindrome(string))
            self.assertTrue(isPalindrome2(string))
        for string in self.notPalindromes:
        	self.assertFalse(isPalindrome(string))
        	self.assertFalse(isPalindrome2(string))

if __name__ == "__main__":
    unittest.main()
