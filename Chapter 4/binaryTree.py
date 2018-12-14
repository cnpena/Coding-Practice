#Simple implementation of a binary tree and the 3 different traversals
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

#Prints the left child, parent and then right child.
#In a binary tree, this prints in ascending order
def inOrderTraversal(node):
	if node:
		inOrderTraversal(node.left)
		print(node.value)
		inOrderTraversal(node.right)

#Prints the parent, left and then right child.
def preOrderTraversal(node):
	if node:
		print(node.value)
		preOrderTraversal(node.left)
		preOrderTraversal(node.right)

#Prints the left and right children and then parent node.
def postOrderTraversal(node):
	if node:
		postOrderTraversal(node.left)
		postOrderTraversal(node.right)
		print(node.value)

root = Node(2)
root.left = Node(1)
root.right = Node(3)

#1 2 3
inOrderTraversal(root)

#2 1 3
preOrderTraversal(root)

#1 3 2
postOrderTraversal(root)
