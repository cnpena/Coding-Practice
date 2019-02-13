#Chapter 4: Trees and Graphs
#4.2 Minimal Tree
#Given an array of integers in sorted increasing order, creates a binary search
#tree with minimal height.
#First notice that to create a tree of minimal height, we need to match the number
#of nodes in the left subtree to the number of nodes in the right subtree as much 
#as possible. So we construct the tree as follows: the middle of each subsection
#becomes the root of the node. The left half becomes the left subtree and the right
#half becomes the right subtree. 

#To do this in an efficient manner, we recursively call the createMinimalBST method
#which is passed a subsection of the array and returns the root of a minimal tree for
#that subsection.
#	Insert into the tree the middle element of the array
#	Insert into the left subtree the left subarray elements
#	Insert into the right subtree the right subarray elements.
#	Recurse

import unittest
from binaryTree import Node

def createMinimalBST(array, start, end):
	if (end < start):
		return None
	mid = (start + end) // 2
	node = Node(array[mid])
	node.left = createMinimalBST(array, start, mid-1)
	node.right = createMinimalBST(array, mid+1, end)
	return node

array = [1, 2, 3, 4, 5]
print(createMinimalBST(array, 0, len(array)-1).value)