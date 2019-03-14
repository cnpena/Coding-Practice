# Cycle Detection 
# Given the head of a linked list, detect if there is a loop in the list
# This code on it's own doesn't work but has been tested on Hackerrank

# Method 1: Fast & Slow Runner
# Works by using a slow and fast runner. The fast runner moves twice as fast as the slow.
# If there is a cycle in the list, the fast runner will catch up with the slow runner, 
# thus indicating the presence of a loop. O(n)

def has_cycle(head):
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Method 2: Hash Table
# Iterates through the list, placing the nodes into a hash table. 
# If current.next exists in the hash table already, must be a loop, return true. O(n)
def has_cycle2(head):
    current = head
    table = set()
    while(current):
        if current.next in table:
            return True
        table.add(current)
        current = current.next
    return False

