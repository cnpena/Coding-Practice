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

    # Do da stuff for returning
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
    def test1(self):
        tree = BinarySearchTree()
        t = 7
        arr = [3, 5, 2, 1, 4, 6, 7]

        for i in range(t):
            tree.create(arr[i])

        self.assertEqual(height(tree.root), 3)
    def test_single_node(self):
        tree = BinarySearchTree()
        t = 1
        arr = [15]

        for i in range(t):
            tree.create(arr[i])

        self.assertEqual(height(tree.root), 0)

if __name__ == "__main__":
    unittest.main()
