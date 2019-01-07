#Two Strings
#Given two strings, determines if they share a common substring.
import unittest

#Since a substring may be as small as one character, 
#puts all characters in string1 in a hash table. Then, if any 
#characters in string2 are in the hash table, returns true

def twoStrings(s1, s2):
    table = {}

    for char in s1:
        table[char] = 1
    for char in s2:
        if char in table:
            return True
    return False

#Alternate solution that uses the intersection operation.
#Returns true if the intersection is at least 1 character,
#false if the intersection set is empty

def findIntersection(s1, s2):
    return not len(set(s1) & set(s2)) == 0

class Test(unittest.TestCase):
    def test_single_letter(self):
        self.assertTrue(twoStrings('hello', 'hi'))
        self.assertTrue(findIntersection('hello', 'hi'))

    def test_double_letters(self):
        self.assertTrue(twoStrings('hello', 'lip'))
        self.assertTrue(findIntersection('hello', 'lip'))

    def test_multiple_letters(self):
        self.assertTrue(twoStrings('hello', 'world'))
        self.assertTrue(findIntersection('hello', 'world'))

    def test_no_letters(self):
        self.assertFalse(twoStrings('hi', 'world'))
        self.assertFalse(findIntersection('hi', 'world'))

if __name__ == "__main__":
    unittest.main()