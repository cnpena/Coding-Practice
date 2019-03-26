# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class Solution(object):
    # Converts x into a string, reverses it and compares to the original. 
    # If they are equal, must be a palindrome.
    def isPalindrome(self, x):
        stringx = str(x)
        reversed = ''
        for i in stringx: 
            reversed = i + reversed
            
        return reversed == stringx
    
    # Keeps x as an integer and builds up the reversed number.
    def isPalindrome2(self, x):
        if x < 0:
            return False
        original = x
        reversed = 0
        
        while x != 0:
            reversed = (reversed*10) + (x%10)
            x = x//10
    
        return original == reversed