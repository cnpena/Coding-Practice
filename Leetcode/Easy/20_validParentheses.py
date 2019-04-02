# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

class Solution(object):
    # Uses a stack to match parenthesis. Iterates through the input string,
    # when an open brace is found, pushes it onto the stack. When a closing brace
    # is found, pops from the stack and checks if they match. The only way a
    # parenthesis pair is valid is if the top of the stack matches the appropriate
    # closing brace. If the stack is empty at the end, there were no extra braces and
    # it must have been a valid string.
    def isValid(self, s):
        stack = []
        table = {'(':')', '[':']', '{':'}'}
        
        for char in s:
            if char in table:
                stack.append(char)
            else:
                if len(stack) == 0 or char != table[stack.pop()]:
                    return False
        return len(stack) == 0
    
    # Uses string manipulation. Goes through and replaces all valid pairs. Returns true only
    # if the empty string is left at the end
    def isValid2(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''