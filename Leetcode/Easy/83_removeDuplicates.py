# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, deletes all duplicates such that each element appear only once.
# Does not have driver code but has been tested on Leetcode.
# Reference: https://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/

# Iterates through the list, checking the current value against the value
# of the node after it. If they are equal, can effectively eliminate the second
# node by changing the next pointer to skip the next node and point to the next
# next node. O(n) time, O(1) space.

def deleteDuplicates(self, head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head