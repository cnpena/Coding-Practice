# Find Merge Point of Two Lists
# Given pointers to the head nodes of 2 linked lists that merge together at some point,
# find the node where the two lists merge.
# This code on it's own doesn't work but has been tested on Hackerrank.


# Hash table
# Works by using a hash table to store all nodes of list1.
# Then, traverses through list2, checking each node to see if it is in the table.
# Returns when it has found the first node that matches.
def findMergeNode(head1, head2):
    #Traverse first list, place all nodes in a table
    current = head1
    table = set()
    while current:
        table.add(current)
        current = current.next

    #Traverse second list until the converging point is found
    current = head2
    while current:
        if current in table:
            return current.data
        current = current.next
