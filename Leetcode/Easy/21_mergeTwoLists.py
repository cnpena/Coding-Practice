# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

class Solution(object):
    # Since the two lists are sorted already, can iterate through each of them, 
    # compare the current values, inserting the smaller value each time into the
    # output list. Creates a dummy head that will point to the output list.
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(0)
        current = dummyHead #Points to the current node as we insert
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next
            
        return dummyHead.next