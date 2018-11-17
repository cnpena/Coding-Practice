#Chapter 2: Linked Lists
#2.7 Intersection, page 95
#Given two singly linked lists, determines if the two lists
#intersect. Returns the intersecting node. 

#Solution 1: Brute Force, for each node in list1, we check if 
#this node is in list2 by linear scanning list2.
#Run time: O(mn), space: O(1)

#Solution 2: Hash Table, Can test whether some node in A is in
#B in O(1) time by keeping the address of each node in B in a hash table.
#O(n) time to insert all the node addresses of list B. Then linear scan A
#Run time: O(m+n), space: O(n)

#Solution 3: Optimal, If two linked list are of equal length, they could
#be scanned at the same pace, and the intersection would be found when they 
#encounter with each other. Works by first finding the length of both list1 
#and list2. Move the pointer of the longer list k nodes ahead so they are
#at the same pace. Finally, iterate through them until we find the same node
from LinkedList import LinkedList
import unittest

def findIntersection(list1, list2):
	if list1.tail is not list2.tail:
		return False

	list1Len = len(list1)
	list2Len = len(list2)

	shorter = list1 if list1Len < list2Len else list2
	longer = list1 if list2Len < list1Len else list2

	difference = abs(list1Len-list2Len)
	#move pointer down on longer list to match shorter list
	longer = getKthNode(list1, difference) if list1Len > list2Len else getKthNode(list2, difference)

	shorterNode, longerNode = shorter.head, longer.head
	
	while(shorterNode is not longerNode):
		shorterNode = shorterNode.next
		longerNode = longerNode.next

	return longerNode.data

def getKthNode(list, k):
	current = list.head
	while(k > 0 and current):
		current = current.next
		k -=1
	return current

list1 = LinkedList()
list2 = LinkedList()

list1.insert('3')
list1.insert('1')
list1.insert('5')
list1.insert('9')

list2.insert('5')
list2.insert('9')


print(findIntersection(list1, list2))

