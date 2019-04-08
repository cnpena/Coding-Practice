# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

class Solution(object):
    # Recursive solution: As we move down each level in the tree, subtract the current value
    # from the sum. When a leaf is reached, if it is equivalent to the sum remaining, return 
    # true. Else, perform the same with the left and right children
    # O(n) time
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
