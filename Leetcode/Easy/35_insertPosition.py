# 35. Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

class Solution(object):
    # Iterates through the list of numbers until it finds the target or it finds
    # the first value that is larger than the target. In either case, returns that
    # index. If the target is larger than every value in the list, it will never hit
    # this return and will hit the return at the end of the function which indicates
    # it should be placed at the end of the list. O(n) time, O(1) space.
    def searchInsert(self, nums, target):
        for index, num in enumerate(nums):
            if num == target or num > target:
                return index
        return len(nums)
    
    # Uses binary search until it finds the target or it finds the index it belongs. 
    # O(logn) time, O(1) space
    def searchInsert2(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left