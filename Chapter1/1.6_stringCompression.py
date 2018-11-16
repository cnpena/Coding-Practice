#Chapter 1: Arrays and Strings
#1.6 String Compression, page 91
#Performs a basic string compression using the counts
#of repeated characters. 
#Example: aabcccccaaa becomes a2b1c5a3

#Iterates through the given string, checking the current 
#letter against the next letter. If they're equivalent, keep moving.
#If not, add current letter/count to compressedString and reset currentCount
import unittest

def compress(string):
	currentCount = 0
	compressedString = ''

	for i in range(len(string)):
		currentCount +=1
		if((i+1 >= len(string)) or string[i] != string[i+1]):
			compressedString = compressedString + string[i] + str(currentCount)
			currentCount = 0

	if(len(compressedString) < len(string)):
		return compressedString
	else:
		return string

#If we only care about number of occurrences, not order:
#Utilizes hash table to keep track of number of occurences of each letter.
#Iterates through hash table to build a string
def compress2(string):
	table = createHashTable(string)
	compressedString = ''
	for key in table:
		compressedString = compressedString + key + str(table[key])
	if(len(compressedString) < len(string)):
		return compressedString
	else:
		return string

def createHashTable(string):
	table = {}
	for letter in string:
		if(letter in table):
			table[letter] +=1
		else:
			table[letter] = 1
	return table

class Test(unittest.TestCase):
    data1 = [ ('aabcccccaaa', 'a2b1c5a3'),
        	('abcd', 'abcd'),
        	('aaabbbcccddd', 'a3b3c3d3') ]

    data2 = [ ('aabcccccaaa', 'a5b1c5'),
        	('abcd', 'abcd'),
        	('aaabbbcccddd', 'a3b3c3d3') ]

    def testCompression(self):
        for [string, expected] in self.data1:
            self.assertEqual(compress(string), expected)
        for [string, expected] in self.data2:
        	self.assertEqual(compress2(string), expected)

if __name__ == "__main__":
    unittest.main()