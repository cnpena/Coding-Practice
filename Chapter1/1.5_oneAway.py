#Chapter 1: Arrays and Strings
#1.5 One Away, page 91
#There are three types of edits that can be performed on strings:
	#1. Insert a character
	#2. Remove a character
	#3. Replace a character
#Given two strings, checks if they are one edit (or zero edits) away
import unittest

def checkOneAway(string1, string2):
	if(len(string1) == len(string2)):
		return checkForReplacement(string1, string2)
	elif(len(string1) == len(string2)-1):
		return checkForInsertion(string1, string2)
	elif(len(string1) == len(string2)+1):
		return checkForInsertion(string2, string1)
	else:
		return False

#For a replacement edit, must have at most one different letter
#between them. To check for this, iterates through the strings,
#using foundDifference to keep track of whether we've found the 
#difference or not already.
def checkForReplacement(string1, string2):
	foundDifference = False
	for i in range(len(string1)):
		if(string1[i] != string2[i]):
			if(foundDifference): 
				return False
			foundDifference = True
	return True

#For an insertion/deletion edit (inverses of each other), must 
#have at most one different letter between them. To check for this, 
#iterates through the strings, skipping the difference in the longer string.
def checkForInsertion(string1, string2):
	index1 = 0
	index2 = 0
	while(index1 < len(string1) and index2 < len(string2)):
		if(string1[index1] != string2[index2]):
			if(index1 != index2): #if unequal, we've already found a difference
				return False
			index2 +=1
		else:
			index1 +=1
			index2 +=1
	return True

class Test(unittest.TestCase):
    data1 = [
        ('pale', 'ple'),
        ('pales', 'pale'),
        ('pale', 'bale'),
        ('Longer string?', 'Longer string'),
        ('', 'd'),
        (' ', ' ')]

    data2 = [
        ('pale', 'plll'),
        ('pales', 'bale'),
        ('ppple', 'apples'),
        ('Longer string?', 'Longer'),
        (' ', 'abc')]

    def testPalindrome(self):
        for string in self.data1:
            self.assertTrue(checkOneAway(*string))
        for string in self.data2:
        	self.assertFalse(checkOneAway(*string))

    if __name__ == "__main__":
    	unittest.main()
