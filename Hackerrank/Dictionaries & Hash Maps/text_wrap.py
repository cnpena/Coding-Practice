# Merge The Tools
# Given a string s and an integer k, splits s into n/k substrings where each 
# substring consists of k characters of s. Within each substring, repeat characters
# are removed such that each character occurs only once within each substring
# Constraints (specified in problem statement): Guaranteed that n is a multiple of k.

def merge_the_tools(string, k):
    while string:
        s = string[0:k]
        seen = set()
        output = ''
        for char in s:
            if char not in seen:
                seen.add(char)
                output +=char
        print(output)
        string = string[k:]