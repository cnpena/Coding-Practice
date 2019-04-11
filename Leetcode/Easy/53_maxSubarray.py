# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

class Solution(object):
	# Iterate through input values, for each value: update currentSum to reflect which is larger:
	# the value itself or the largest sum of previous values + current value. O(n) time, O(1) space
	def maxSubArray(self, nums):
	    maxValue = nums[0]
	    currentSum = nums[0]
	    
	    for value in nums[1:]:
	        currentSum = max(value, currentSum+value)
	        maxValue = max(currentSum, maxValue)
	    return maxValue

