# 58. Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the
# length of last word in the string.
# If the last word does not exist, return 0.

class Solution(object):
    # Uses the string split method to put all words into an array. The last word will
    # simply be the last item in the array and we can return the length of that
    # last item. O(n) time, O(n) space
    def lengthOfLastWord(self, s):
        array = s.split()
        if len(array) == 0:
            return 0
        words = array[len(array)-1]
        return len(words)
    
    # Iterates through the characters of the string starting at the end. First while
    # loop skips any white spaces at the end. The second while loop iterates through
    # the characters of the last word, counting each letter. Once we hit a space, 
    # we've found the beginning of the word and returns the length.
    def lengthOfLastWord2(self, s):
        length = 0
        index = len(s)-1 #start at the last char

        while index >=0 and s[index] == ' ':
            index -=1
        while index >= 0 and s[index] != ' ':
            length +=1
            index -=1
        return length