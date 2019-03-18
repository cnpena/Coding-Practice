# 67. Add Binary
# Given two binary strings, return their sum (also a binary string).
# No driver code but has been tested on Leetcode
# Reference: https://www.geeksforgeeks.org/program-to-add-two-binary-strings/

# To add binary numbers, start at the right end of both numbers, iterating to the 
# front. Each iteration, add the value of each number at that index plus the value of the
# carry (if any). 
def addBinary(self, a, b):
    result = ''
    currentA = len(a)-1
    currentB = len(b)-1
    carry = 0
    
    while currentA >= 0 or currentB >= 0:
        x = a[currentA] if currentA >= 0 else 0
        y = b[currentB] if currentB >= 0 else 0
        
        sum = int(x) + int(y) + carry # raw sum value
        carry = sum//2 # value that needs to be carried, 0 or 1
        result = str(sum%2) + result # update result string
        
        currentA -=1
        currentB -=1
    
    if carry > 0: # in case that there is one last carry that makes the string 1 digit longer than the input numbers
        result = str(carry) + result
    return result