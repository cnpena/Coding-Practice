# Checks if they are equivalent by performing an inOrderTraversal through both trees
# If we come upon a node that is not consistent between trees, return False.
class Solution(object):
    def isSameTree(self, p, q):
        return inOrderTraversal(p,q)
        
    
def inOrderTraversal(node1, node2):
    if node1 and node2:
        inOrderTraversal(node1.left, node2.left)
        if (node1.val != node2.val):
            return False
        inOrderTraversal(node1.right, node2.right)
    return True
        