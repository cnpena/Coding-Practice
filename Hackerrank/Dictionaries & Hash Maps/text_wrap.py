# Merge The Tools
# Given a string s and an integer k, splits s into n/k substrings where each 
# substring consists of k characters of s. Within each substring, repeat characters
# are removed such that each character occurs only once within each substring
# Constraints (specified in problem statement): Guaranteed that n is a multiple of k.

# This solution works by iterating through the string. At each iteration,
# we look at the k characters in the substring. A set is used to prevent 
# duplicate values from being printed in each substring with O(1) lookup. 
# If a character is not a duplicate, it is added to the output string which
# is printed when the whole substring has been looked at.
def merge_the_tools(string, k):
    while string:
        s = string[0:k] # Get substring of length k
        seen = set()
        output = ''

        for char in s:
            if char not in seen:
                seen.add(char) # Add char to set and output string
                output +=char
        print(output)
        string = string[k:] # Move to next k characters

string1 = 'ABCDEFGHI'
string2 = 'AABCAAADA'
k = 3
print(merge_the_tools(string1, k))
print(merge_the_tools(string2, k))