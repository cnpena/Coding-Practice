# 27. Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and 
# return the new length.

class Solution(object):
    # Iterate through the array using two pointers. i is the slow runner, j is the
    # fast runner. If the value at j equals the given value, can effectively skip to
    # the next value (that's not val) and copy to the value at i. 
    def removeElement(self, nums, val):
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
        return i
