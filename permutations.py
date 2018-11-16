#Chapter 1: Arrays and Strings
#1.2 CheckPermutation, page 90
#Given two strings, checks if one is a permutation of the other
#Notes: For interview, should ask if case sensitive, whitespace

#Sorts the two strings, checks if the sorted lists are equivalent
#Returns false immediately if the strings are not the same length
#Run time: O(n log n)
import unittest

def checkPermutation(string1, string2):
	if(len(string1) != len(string2)):
		return False

	return sorted(string1) == sorted(string2)

#Iterates through each string, returns false if we reach
#a character that is not present in the other string
#Returns false immediately if the strings are not the same length
#Run time: O(n^2), space O(1)
def checkPermutation2(string1, string2):
	if(len(string1) != len(string2)):
		return False

	for letter in string1:
		if(letter not in string2):
			return False
	for letter in string2:
		if(letter not in string1):
			return False
	return True

#Utilizes a hash table (dictionary), mapping each char to frequency
#Iterates through string1, saving the number of occurrences for each
#letter. Then, iterates through string2, decrementing the value of each letter
#Terminates early if any value ever turns negative 
#Run time: O(n), space: O(n)
def checkPermutation3(string1, string2):
	if(len(string1) != len(string2)):
		return False
	table = {}
	for letter in string1:
		if(letter not in table):
			table[letter] = 1
		else:
			table[letter] = table[letter] + 1
	for letter in string2:
		if(letter in table):
			table[letter] = table[letter] - 1
			if(table[letter] < 0): return False
		else:
			return False
	return True

class Test(unittest.TestCase):
    data1 = [ ('1234567', '7654321'), 
    		('happy', 'hppay'),
    		('coding' , 'gnciod') ]

    data2 = [('1234567', '12345678'),
    		('happy', 'hpppy'),
    		('coding', 'gnidcc')]

    def testPermutations(self):
        #Should return true
        for string in self.data1:
            self.assertTrue(checkPermutation(*string))
            self.assertTrue(checkPermutation2(*string))
            self.assertTrue(checkPermutation3(*string))
        #Should return false
        for string in self.data2:
            self.assertFalse(checkPermutation(*string))
            self.assertFalse(checkPermutation2(*string))
            self.assertFalse(checkPermutation3(*string))

if __name__ == "__main__":
    unittest.main()

