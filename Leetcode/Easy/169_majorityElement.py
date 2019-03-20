# Given an array of size n, find the majority element. You may assume that the array is non-empty 
# and the majority element always exist in the array.
# Reference: https://www.geeksforgeeks.org/majority-element/
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
    # If no guarantee that there is a majority element, cannot definitively say that it is in the
    # middle.
    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
    # Slight augment of above solution but works even if there is no guarantee to be a majority
    # element. Same logic applies that if there is a majority element, it will be the middle.
    # But, if there is no guarantee, this could also not be a majority element. Therefore, all
    # we need to do is iterate through the list once, counting the occurences of the potential
    # majority element. If if exists more than n//2 times, return. If after counting we haven't
    # counted n//2 of potential element, cannot be a majority and return None.
    def majorityElement3(self, nums):
        nums.sort()
        
        potentialMiddle = nums[len(nums)//2]
        count = 0
        for i in nums: # count number of occurences of potentialMiddle
            if i == potentialMiddle:
                count +=1
                if count > len(nums)//2:
                    return i
        return None

    # Uses the majority voting algorithm to solve this problem. Start by arbitrarily assigning
    # the first element to be the potential majority element. Each iteration, add 1 to count if 
    # we come accross another instance of this value. For every other value, minus 1 to count. 
    # If this value is not the actual majority, the count will reduce to 0 at some point and 
    # a new potential majority will be chosen. Continues until the end of the list where potential
    # majority variable will contain the value of the potential majority. When it is not guaranteed
    # that there is a majority element, simply need to iterate once more and count the occurences of
    # majority element. O(n) time, O(1) time
    
    def majorityElement(self, nums):
        count = 0
        potentialMajority = None
        
        for value in nums:
            if count == 0:
                potentialMajority = value
            if value == potentialMajority:
                count +=1
            else:
                count -=1
        return potentialMajority
        