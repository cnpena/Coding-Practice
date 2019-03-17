 # 69. Sqrt(x)
 # Given a value x, find the floor of the square root of x. 
 # No driver code but has been tested on Leetcode.
 # Reference: https://www.geeksforgeeks.org/square-root-of-an-integer/
 
 # Tries all numbers from 1 to x. Once it comes upon the first value squared
    # that is larger than x, the previous value must be the floor of the square
    # root of x. O(sqrt(n)) time, O(1) space 
    def mySqrt(self, x):
        i = 0
        while(i <= x):
            if i*i > x:
                return i-1
            i +=1
        return i-1
    
    # Uses binary search to find the floor of the square root. Compares the middle
    # value squared to x to determine which half to look at. O(logx) time O(1) space
    def mySqrt(self, x):
        left = 0
        right = x
        square = 0
        
        while (left <= right):
            mid = (left + right)//2
            squared = mid*mid
            
            if squared == x: # x is a perfect square
                return mid
            elif squared < x: # since we are searching for the floor of value, update when less than x.
                left = mid+1
                square = mid
            else:
                right = mid-1 # mid*mid is greater than x
        return square