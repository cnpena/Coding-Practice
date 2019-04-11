# 38. Count and Say
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

class Solution(object):
    # Builds up the solution by iterating through the output string, keeping track of
    # the number of consecutive characters. When the same char is seen, count is
    # incremented. When a different char is seen, the current string must be updated, 
    # the new char saved as the new value to count and the count reset to 1. 
    def countAndSay(self, n):
        output = '1'
        
        for _ in range(n-1):
            currentChar = output[0] #start at the beginning of the string
            count = 0
            currentString = ''
            
            for char in output:
                if char == currentChar:
                    count +=1 #continue to next iteration
                else:
                    currentString += str(count) + currentChar #update to count,value
                    currentChar = char #reset currentChar
                    count =1    #reset count
            currentString += str(count) + currentChar
            output = currentString
        return output
                    
                    
            