#Two Strings
#Given two strings, determines if they share a common substring.
#Since a substring may be as small as one character, 
#puts all characters in string1 in a hash table. Then, if any 
#characters in string2 are in the hash table, returns true
import unittest

def twoStrings(s1, s2):
    table = {}

    for char in s1:
        table[char] = 1
    for char in s2:
        if char in table:
            return True
    return False

class Test(unittest.TestCase):
    def test_single_letter(self):
        self.assertTrue(twoStrings('hello', 'hi'))

if __name__ == "__main__":
    unittest.main()