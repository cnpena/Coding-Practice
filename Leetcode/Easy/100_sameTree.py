# 100. Same Tree
# Given two binary trees, checks if they are the same or not.
# Contains no driver code but has been tested on Leetcode.

# Checks if they are equivalent by performing a recursive traversal through both trees
# O(n) time, O(logn) / O(n) space depending on how balanced the tree is.
# Reference: https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: #if both null, continue
            return True
        
        if not p or not q: #if only one is null, cannot be same, return false
            return False
    
        if p.val != q.val: #if they have different values, cannot be same, return false
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        