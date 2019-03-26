# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up 
# to a specific target.

class Solution(object):
    # Absolute brute force is to iterate through the list, for each value, see if
    # the target-value exists in the list. If so, find and return the two indices. 
    # O(n) time, O(1) space
    def twoSum1(self, nums, target):
        for index, value in enumerate(nums):
            otherValue = target-value
            try: 
                foundIndex = nums.index(otherValue)
                if foundIndex != index:
                    return (index, foundIndex)
            except ValueError: 
                print('not found')
            
    # Iterate through list, put each value in a hash table. Iterate once more, for
    # each value, check if the complement exists in the hash table. If so, return. 
    # O(n) time, O(n) space
    def twoSum2(self, nums, target):
        table = {}
        for index, value in enumerate(nums):
            table[value] = index
            
        for index, value in enumerate(nums):
            otherValue = target-value
            if otherValue in table:
                if index != table[otherValue]:
                    return (index, table[otherValue])
        return 'No two sum solution'
    
    # Iterate through the list, put each value in a hash table. As you iterate,
    # check if the complement exists in the hash table. If so, return. 
    # O(n) time, O(n) space. A little faster than the second solution.
    def twoSum3(self, nums, target):
        table = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in table:
                return (index, table[complement])
            table[value] = index
        return 'No two sum solution'

