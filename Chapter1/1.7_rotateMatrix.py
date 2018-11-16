#Chapter 1: Arrays and Strings
#1.7 Rotate Matrix, page 91
#Given an image represented by an NxN matrix, where each pixel 
#in the image is 4 bytes, rotates the image by 90 degrees.

#Rotates a matrix counterclockwise 
#starts at each corner and swaps values, moving toward center
#Essentially goes layer by layer
import unittest

def rotate(matrix):
	n = len(matrix)

	for i in range(int(n/2)):
		for j in range(i, n-1-i):
			temp = matrix[i][j]

			#move from top right to top left
			matrix[i][j] = matrix[j][n-1-i]

			#move from bottom right to top right
			matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
			
			#move from bottom left to bottom right
			matrix[n-1-i][n-1-j] = matrix[n-1-j][i] 
			
			#bottom left gets top left value (temp)
			matrix[n-1-j][i] = temp
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
				[5, 6, 7, 8], 
				[9, 10, 11, 12 ], 
				[13, 14, 15, 16 ]] 

	mat2Expected = [[4, 8, 12, 16], 
					[3, 7, 11, 15], 
					[2, 6, 10, 14], 
					[1, 5, 9, 13]] 

	mat3Input = [[1, 2, 3], 
				[4, 5, 6], 
				[7, 8, 9]]

	mat3Expected = [[3, 6, 9], 
					[2, 5, 8], 
					[1, 4, 7]] 

	mat4Input = [[1, 2 ], 
				[3, 4 ]]

	mat4Expected = [[2, 4 ], 
					[1, 3 ]]

	data = [(mat1Input, mat1Expected),
			(mat2Input, mat2Expected),
			(mat3Input, mat3Expected),
			(mat4Input, mat4Expected)]

	def testRotateMatrix(self):
		for [matrix, expected] in self.data:
			self.assertEqual(rotate(matrix), expected)

if __name__ == "__main__":
	unittest.main()
 

