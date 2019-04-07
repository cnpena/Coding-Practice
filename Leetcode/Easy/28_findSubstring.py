# 28. Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack.

class Solution(object):
    # Iterates through the haystack. For each i, checks if the substring at 
    # i:i+len(needle) is the needle. If so, return i immediately. If not, continues
    # on to the next i. If the return is never hit, returns -1 to indicate that 
    # the needle was not in the haystack.
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1