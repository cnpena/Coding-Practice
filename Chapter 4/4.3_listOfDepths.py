#Chapter 4: Trees and Graphs
#4.3 List of Depths, page 109
#Given a binary tree, creates a linked list of all of the nodes at each depth

from binaryTree import Node as TreeNode

def createLevelLinkedList(root, lists, level):
	if not root:
		return

	list = None
	if len(lists) == level:
		list = []
		lists.append([])
	else:
		list = lists[level]

	list.append(root)

	createLevelLinkedList(root.left, lists, level+1)
	createLevelLinkedList(root.right, lists, level+1)

	return lists

ten = TreeNode(10)
eight = TreeNode(8)
twelve = TreeNode(12)
ten.left = eight
ten.right = twelve

sol = createLevelLinkedList(ten, [], 0)
for i in sol:
	for j in i:
		print(j.value)





