# Given an array of size n, find the majority element. You may assume that the array is non-empty 
# and the majority element always exist in the array.
from collections import defaultdict
class Solution(object):
    # Really a problem of keeping count of an unknown number of elements. Can keep track of count
    # of each element in list using a hash table. While iterating through list, if the current
    # element has a count of n//2, return immediately. O(n) time, O(n) space
    def majorityElement(self, nums):
        table = defaultdict(int)
        for i in nums:
            table[i] +=1
            if table[i] > len(nums)//2:
                return i
        return None

    # Can solve this problem by sorting the list. If there is a majority element, it must be present
    # at nums[n/2]. O(nlogn) time, O(1) space
    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums)//2]