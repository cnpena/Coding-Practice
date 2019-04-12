# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    
    # Brute force solution
    # Take all possible step combinations (1 and 2) at every step. At every step, call the
    # climb stairs for each and return the sum of the return values. O(2^n) time, O(n) space
    def climbStairs(self, n):
        return self.climbStairs_rec(0, n)
        
    def climbStairs_rec(self, i, n):
        if i > n:
            return 0
        
        if i == n:
            return 1
        
        return self.climbStairs_rec(i+1, n) + self.climbStairs_rec(i+2, n)
    # Variable a tells you the number of ways to reach the current step, and b tells you the number of ways to reach the next step. So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.
    def climbStairs(self, n):
        a = 1
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a