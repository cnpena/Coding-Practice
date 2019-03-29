# 14. Longest Common Prefix
# Finds the longest common prefix string amongst an array of strings.
# If there is no common prefix, returns an empty string.

class Solution(object):
    # Works by iterating through the characters in the first string in the list.
    # For each character, checks all other strings in the list to see if the
    # character at the same index matches. Stops when it reaches the end of the
    # string or one of the strings doesn't match. In this case, returns a string
    # containing the letters that have been matched.
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        
        for i in range(len(strs[0])):
            currentChar = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or currentChar != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]