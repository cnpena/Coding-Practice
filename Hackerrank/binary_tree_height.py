#Returns the height of a binary tree, the number of edges between
#the tree's root and it's furthest leaf.

import unittest

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    height = visit(root, 0, 0)
    return height
    
def visit(root, current, maxHeight):
    maxDepthL = 0
    maxDepthR = 0

    if root.left:
        maxDepthL = visit(root.left, current + 1, maxHeight)
    if root.right:
        maxDepthR = visit(root.right, current + 1, maxHeight)

    #Determine what value to return
    if(maxDepthL and maxDepthR):
        return max(maxDepthL, maxDepthR)
    elif(maxDepthL):
        return maxDepthL
    elif(maxDepthR):
        return maxDepthR
    else: # The node is a leaf
        maxHeight = max(current, maxHeight)
        return maxHeight

class Test(unittest.TestCase):
    test1 = [1]
    test2 = [2, 1]
    test3 = [1, 2]
    test4 = [2, 1, 3]
    test7 = [4, 1, 2, 3, 5, 6, 7]

    #Binary tree with a single node should return height 0
    def test_single_node(self):
        tree = BinarySearchTree()

        for i in range(len(self.test1)):
            tree.create(self.test1[i])

        self.assertEqual(height(tree.root), 0)

    #Binary tree with one root and one left child
    def test_left_child_only(self):
        tree = BinarySearchTree()

        for i in range(len(self.test2)):
            tree.create(self.test2[i])

        self.assertEqual(height(tree.root), 1)

    #Binary tree with one root and one right child
    def test_right_child_only(self):
        tree = BinarySearchTree()

        for i in range(len(self.test3)):
            tree.create(self.test3[i])

        self.assertEqual(height(tree.root), 1)

    #Binary tree with 3 nodes, filled tree
    def test_full_tree_3_nodes(self):
        tree = BinarySearchTree()

        for i in range(len(self.test4)):
            tree.create(self.test4[i])

        self.assertEqual(height(tree.root), 1)

    #Binary tree with 7 nodes, a full tree
    def test_full_tree(self):
        tree = BinarySearchTree()

        for i in range(len(self.test7)):
            tree.create(self.test7[i])

        self.assertEqual(height(tree.root), 3)

if __name__ == "__main__":
    unittest.main()
