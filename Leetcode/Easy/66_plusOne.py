# 66. Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each
# element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution(object):
    # Iterates backward through the digits, carrying over any value if necessary.
    # This solution works for a more general case ie adding more than 1 to the list.
    # For this specific problem, the second solution works faster.
    def plusOne(self, digits):
        n = len(digits)
        current = n-1

        carry = 1
        while carry != 0 and current >= 0:
            value = carry + digits[current]
            carry = value//10
            digits[current] = value%10
            current -=1
        if carry > 0:   # If there is a carry on the last value, need to insert a new index in front
            digits.insert(0, carry)
        return digits
    
    # Iterates backward through the array, continuing only if it is necessary (if the value is 9, therefore a carry is necessary)
    def plusOne2(self, digits):
        n = len(digits)-1
        
        for i in range(n, -1, -1):
            if digits[i] < 9:
                digits[i] +=1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits