#Chapter 1: Arrays and Strings
#1.1 isUnique, page 90
#Determines if a string has all unique characters.

#Iterates through the given string, putting each letter into
#a hash table (dictionary). Immediately returns false if it 
#comes upon a letter that has already been seen
# Run time: O(n), space: O(n),
#Dictionaries have O(1) lookup time in Python
import unittest

def isUnique(string):
	table = {}
	for letter in string:
		if(letter in table):
			return False
		else:
			table[letter] = 1
	return True

#Uses set to eliminate any duplicate characters.
#If the length of that set is the same as the length of the 
#original string, then you have entirely unique characters.
def isUnique2(string):
    return len(set(string)) == len(string)

#If you can't use data structures:
	# 1. Compare every character of the string to every other character.
		# O(n^2) time and O(1) space.
	# 2. If we can modify the input string, can sort the string in 
		# O(n log n) and linearly check neighboring characters

#Deletes duplicate characters from a string
#Iterates through the given string, putting each letter into a hash table 
#(dictionary). If the char hasn't been seen yet, appends to a new string
#to return
#Run time: O(n), space: O(n)
def deleteDuplicates(string):
	table = {}
	newString = ''
	for letter in string:
		if(letter not in table):
			newString  = newString + letter
			table[letter] = 1
	return newString

class Test(unittest.TestCase):
    data1 = [('1234567'), ('water'), ('')]
    data2 = [('1234abcd1'), ('applesauce')]

    def testForUnique(self):
        #Should return true
        for string in self.data1:
            self.assertTrue(isUnique(string))
            self.assertTrue(isUnique2(string))
            self.assertTrue(len(set(string)) == len(deleteDuplicates(string)))
        #Should return false
        for string in self.data2:
            self.assertFalse(isUnique(string))
            self.assertFalse(isUnique2(string))

if __name__ == "__main__":
    unittest.main()



