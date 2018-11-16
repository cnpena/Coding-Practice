#Chapter 1: Arrays and Strings
#1.9 String Rotation, page 91
#Given 2 strings, string1 and string2, checks if
#string2 is a rotation of string1. 
#Uses only one call to isSubstring, a method that checks if
#one word is a substring of another.

#In a rotation, we cut string1 into two parts, x and y, rearranging
#to get string2.
#Example: 
# string1 = waterbottle
# x = wat
# y = erbottle
# string2 = yx = erbottlewat
#Need to check if there's a way to split string1 into x and y such that
#xy = string1 and yx = string2
#Regardless of where the division between x and y is, yx will always be
#a substring of xyxy. string2 will always be a substring of string1string1.
import unittest

def isRotation(string1, string2):
	if(len(string1) == len(string2)): #must be equal lengths to be a rotation
		xyxy = string1+string1
		return(string2 in xyxy)
	return False


class Test(unittest.TestCase):
	data1 = [('waterbottle', 'erbottlewat'),
			('apples', 'lesapp'),
			('interview', 'wintervie'),
			('rot-ation', '-ationrot')]

	data2 = [('waterbottle', 'bottleerwat'),
			('apples', 'selppa'),
			('interview', 'interviwe'),
			('rot-ation', 'rotation')]

	def testStringRotation(self):
		for [string, rotatedString] in self.data1:
			self.assertTrue(isRotation(string, rotatedString))
		for [string, rotatedString] in self.data2:
			self.assertFalse(isRotation(string, rotatedString))

if __name__ == "__main__":
	unittest.main()