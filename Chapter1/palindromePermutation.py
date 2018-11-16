#Chapter 1: Arrays and Strings
#1.4 Palindrome Permutation, page 91
#Given a string, determines whether it is a permutation of a palindrome.
#A palindrome is a word or phrase that is the same forwards and backwards

#Solution 1: Utilizes a hash table to count the occurrence of each letter
#By definition of a palindrome, can have at most 1 letter with an odd count.
#Run time: O(n) (Can't optimize big O time since any algorithm will always
#have to look through the entire string)
import unittest

def isPermutation(string):
	new = string.replace(' ', '') #ignore spaces
	table = createHashTable(new)
	return(checkHashTable(table))

#Returns a hash table with the count of each letter in the string
def createHashTable(string):
	table = {}

	for letter in string:
		if(letter in table):
			table[letter] +=1
		else:
			table[letter] = 1
	return table

#Iterate through the hash table to ensure that no more than one character 
#has an odd count.
def checkHashTable(table):
	foundOdd = False
	for key in table:
		if(table[key]%2 != 0):
			if(foundOdd): return False
			foundOdd = True
	return True

class Test(unittest.TestCase):
    data = [
        ('taco cat', True),
        ('racecar', True),
        ('Now not Wonton?', True),
        ('No lemon, no melon.', True),
        ('Not a Palindrome', False),
        ('coding codi', False),
        ('A tuna a for of jar nut', True)]

    def testPalindrome(self):
        for [string, expected] in self.data:
            actual = isPermutation(string)
            self.assertEqual(actual, expected)

    if __name__ == "__main__":
    	unittest.main()
