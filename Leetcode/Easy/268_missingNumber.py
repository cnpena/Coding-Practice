# 268. Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array

class Solution(object):
    # Uses the fact that the sum of n numbers will be n(n-1)/2
    # Calculates the sum of the values in the array, the missing value
    # will be the difference between these two values
    # O(n) time, O(1) space
    def missingNumber(self, nums):
        n = len(nums)
        expectedSum = n*(n+1)/2
        actualSum = sum(nums)
        return expectedSum-actualSum
     
    # Uses a hash table to keep track of which values exist in the array.
    # Places each value in hash table, at the end, iterates 0 to n until it finds 
    # the value that doesn't exist in the table.
    # O(n) time, O(n) space
    def missingNumber2(self, nums):
        table = set()
        n = len(nums)
        for num in nums:
            table.add(num)
        for i in range(0, n+1):
            if i not in table:
                return i
    
    # Sorts the list in order to find which value is missing
    # After sorting, does two initial checks on the first and last value
    # If neither of these are missing, iterates through 1 to n-1 until
    # it finds the missing number. Since it is sorted, we know to expect
    # the previous number+1 and can return this value if it does not exist.
    def missingNumber3(self, nums):
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0
        
        for i in range(1,len(nums)):
            expected = nums[i-1]+1
            if nums[i] != expected:
                return expected