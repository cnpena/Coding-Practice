#Simple implementation of a binary tree and the 3 different traversals
import unittest

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

#Prints the left child, parent and then right child.
#In a binary tree, this prints in ascending order
def inOrderTraversal(node, list):
	if node:
		inOrderTraversal(node.left, list)
		list.append(node.value)
		inOrderTraversal(node.right, list)
	return list

#Prints the parent, left and then right child.
def preOrderTraversal(node, list):
	if node:
		list.append(node.value)
		preOrderTraversal(node.left, list)
		preOrderTraversal(node.right, list)
	return list

#Prints the left and right children and then parent node.
def postOrderTraversal(node, list):
	if node:
		postOrderTraversal(node.left, list)
		postOrderTraversal(node.right, list)
		list.append(node.value)
	return list

root = Node(1)

fullTree = Node(2)
fullTree.left = Node(1)
fullTree.right = Node(3)

leftChild = Node(2)
leftChild.left = Node(1)

rightChild = Node(2)
rightChild.right = Node(3)


class Test(unittest.TestCase):
	def test_inOrder_traversal(self):
		self.assertEqual(inOrderTraversal(root, []), [1])
		self.assertEqual(inOrderTraversal(leftChild, []), [1, 2])
		self.assertEqual(inOrderTraversal(rightChild, []), [2, 3])
		self.assertEqual(inOrderTraversal(fullTree, []), [1, 2, 3])

	def test_preOrder_traversal(self):
		self.assertEqual(preOrderTraversal(root, []), [1])
		self.assertEqual(preOrderTraversal(leftChild, []), [2, 1])
		self.assertEqual(preOrderTraversal(rightChild, []), [2, 3])
		self.assertEqual(preOrderTraversal(fullTree, []), [2, 1 , 3])

	def test_postOrder_traversal(self):
		self.assertEqual(postOrderTraversal(root, []), [1])
		self.assertEqual(postOrderTraversal(leftChild, []), [1, 2])
		self.assertEqual(postOrderTraversal(rightChild, []), [3, 2])
		self.assertEqual(postOrderTraversal(fullTree, []), [1, 3 , 2])
		
if __name__ == "__main__":
	unittest.main()
