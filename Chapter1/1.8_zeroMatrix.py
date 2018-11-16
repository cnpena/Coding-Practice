#Chapter 1: Arrays and Strings
#1.8 Zero Matrix, page 91
#Given a matrix, if an element in an MxN is 0, 
#its entire row and column are set to 0.

#Works by first finding the location of the zeros in the matrix.
#then, changes each row and column found in findZeros()
#finally, calls printMatrix to print in an easily readable form
#Run time: O(mn), space O(m+n)
import unittest

def zeroMatrix(matrix):
	rows, columns = findZeros(matrix)
	zeroMatrix = insertZeros(matrix, rows, columns)
	return zeroMatrix

#Iterates through matrix, saving rows and colums where zeros exist
#Performs simple check to prevent saving duplicate rows/colums
def findZeros(matrix):
	rows = []
	columns = []
	for m in range(len(matrix)):
		for n in range(len(matrix[m])):
			if(matrix[m][n] == 0):
				if(m not in rows):
					rows.append(m)
				if(n not in columns):
					columns.append(n)
	return rows, columns

#Iterates through list of rows and columns that need to be converted to zeros,
#Changing the values in the actual matrix to 0
def insertZeros(matrix, rows, columns):
	for row in rows:
		for i in range(len(matrix[row])):
			matrix[row][i] = 0
	for col in columns:
		for j in range(len(matrix)):
			matrix[j][col] = 0
	return matrix

#Prints matrix in an easily readable form
def printMatrix(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end = ' ')
		print('')

class Test(unittest.TestCase):
	mat1Input = [[0 for x in range(4)] for y in range(4)] 
	mat1Expected = [[0 for x in range(4)] for y in range(4)] 

	mat2Input = [[1, 2, 3, 4], 
				[5, 0, 7, 8], 
				[9, 10, 0, 12 ], 
				[13, 14, 15, 16 ]] 

	mat2Expected = [[1, 0, 0, 4], 
					[0, 0, 0, 0], 
					[0, 0, 0, 0], 
					[13, 0, 0, 16]] 

	mat3Input = [[0, 2, 3], 
				[4, 5, 6], 
				[7, 8, 9]]

	mat3Expected = [[0, 0, 0], 
					[0, 5, 6], 
					[0, 8, 9]] 

	mat4Input = [[1, 2 ], 
				[3, 0 ]]

	mat4Expected = [[1, 0 ], 
					[0, 0 ]]

	data = [(mat1Input, mat1Expected),
			(mat2Input, mat2Expected),
			(mat3Input, mat3Expected),
			(mat4Input, mat4Expected)]

	def testZeroMatrix(self):
		for [matrix, expected] in self.data:
			self.assertEqual(zeroMatrix(matrix), expected)

if __name__ == "__main__":
	unittest.main()