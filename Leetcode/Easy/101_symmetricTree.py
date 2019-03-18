# 101. Symmetric Tree
# Given a binary tree, checks whether it is a mirror of itself (ie, symmetric around its center).
# No driver code but has been tested on Leetcode.
# Reference: https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/

class Solution(object):
    # In order to see if two subtrees are symmetric, we need to check if the left subtree
    # is a mirror reflection of the right subtree. Can be defined as mirror reflections
    # if their roots are equal and their right subtree is a mirror reflection of the left
    # subtree of the other. Can check this recursively like so: O(n) time, O(n) space
    def isSymmetric(self, root):
        return self.isMirror(root, root)
        
    def isMirror(self, t1, t2):
        # If both values are None, they are mirror reflections, return True
        if (not t1) and (not t2):
            return True

        # If only one has a nil value, cannot be mirror reflections, return False
        if (not t1) or (not t2):
            return False

        # Otherwise, they both have values and we must compare the values
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
    
    # Iterative solution that uses a queue. Each two consecutive nodes in the queue should be equal
    # Works similarly to BFS except each iteration, two nodes are extracted and their values
    # compared. Then, the right and left children are inserted into the queue in opposite order.
    # Algorithm stops when the queue is empty or we find instance where two subtrees are not
    # symmetric. O(n) time, O(n) space.
    import collections
    
    def isSymmetric2(self, root):
        queue = collections.deque([root, root])
        
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            
            if not t1 and not t2:
                continue
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True