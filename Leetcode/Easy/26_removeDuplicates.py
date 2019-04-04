# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element 
# appear only once and return the new length

class Solution(object):
    # Uses two pointers to iterate through the array. Pointer j will keep moving until
    # it reaches a non duplicate value. When it finds a new value, it copies it into 
    # the next available space which is i+1. Each time a new value is found, count is
    # incremented and returned at the end to represent how many unique values are in
    # the array.
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        count = 1
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1
                count +=1
                nums[i] = nums[j]
        return count