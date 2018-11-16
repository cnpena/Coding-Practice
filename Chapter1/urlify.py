#Chapter 1: Arrays and Strings
#1.3 URLify, page 90
#Replaces all spaces in a string with '%20'
#Assume that you are given the true length of the string
#Example:
	#input: 'Mr John Smith     ', 13
	#output: 'Mr%20John%20Smith'
import unittest

#Uses built in function replace to replace spaces with '%20'
def URLify(string, length):
	string = string[:length]
	return string.replace(' ', '%20')

#Iterates through the string, appending to a new string
#If we hit a space, append '%20', otherwise, copy the char
#Run time: O(n)
def URLify2(string, length):
	newString = ''
	for i in range(length):
		if(string[i] == ' '):
			newString = newString + '%20'
		else:
			newString = newString + string[i]
	return newString

class Test(unittest.TestCase):
    data = [ ('Mr John Smith      ', 13, 'Mr%20John%20Smith'), 
    		('a b   ', 3, 'a%20b'),
    		('coding' , 6, 'coding') ]

    def testURLify(self):
        for string in self.data:
            for [string, length, expected] in self.data:
            	actual = URLify(string, length)
            	self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()