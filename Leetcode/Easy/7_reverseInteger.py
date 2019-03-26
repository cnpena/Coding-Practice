# 7. Reverse Integer 
# Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        max_32 = 2147483647
        min_32 = -2147483648
        
        result = 0
        sign = (x > 0) - (x < 0)
        x = abs(x)
        
        while (x != 0):
            rem = x % 10
            x = x // 10
            result = result * 10 + rem
            
        if((result > max_32) or (result < min_32)):
            return 0

        return result * sign

