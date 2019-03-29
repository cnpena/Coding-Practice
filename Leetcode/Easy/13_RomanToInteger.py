# 13. Roman to Integer
# Given a roman numeral, convert it to an integer
class Solution(object):
    # Makes use of a separate function to return the value of each numeral given.
    # Iterates through the given numerals, getting the value for each. For each
    # numeral, checks whether the value is less than the one to the right of it.
    # ie checks if we have a situation in which we need to subtract. If the current
    # numeral's value is less than the next one, we simply need to subtract the
    # current value from the total. If not, we can simply add it to the total and
    # continue on. 
    def romanToInt(self, s):
        total = 0
        
        for index, numeral in enumerate(s):
            value = getValue(numeral)
            
            if index < len(s)-1 and value < getValue(s[index+1]):
                total -= value
            else:
                total += value
        return total
            
def getValue(numeral):
    if numeral == 'I':
        return 1
    if numeral == 'V':
        return 5
    if numeral == 'X':
        return 10
    if numeral == 'L':
        return 50
    if numeral == 'C':
        return 100
    if numeral == 'D':
        return 500
    if numeral == 'M':
        return 1000
    return 0
        