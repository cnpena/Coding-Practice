# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest 
# path from the root node down to the farthest leaf node.

class Solution(object):
    # Recursive solution: If we've reached a leaf, add 0, 
    # otherwise add 1 + depth of left or right child (whichever is larger)
    # O(n) time

    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
