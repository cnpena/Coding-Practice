#Hourglass Sum
#Given a 6x6 2D array, define an hourglass to be a subset of values
#with indices in this pattern: a b c
#								 d
#							   e f g
#There are 16 hourglasses in the array, and an hourglass is the sum
#of an hourglass' values. This program computes all possible hourglass
#sums and returns the largest hourglass sum.
import unittest

#Works by simply iterating through each possible hourglass and computing the sum.
#If the sum is larger than the current max, set this value as the new max.
def hourglassSum(arr):
	#set initial sum to the first hourglass
	maxSum = sum(arr[0][0:3]) + arr[1][1] + sum(arr[2][0:3])
	for line in range(4):
		for i in range(4):
			top = sum(arr[line][i:i+3]) #sum top row
			middle = arr[line+1][i+1] #value in middle
			bottom = sum(arr[line+2][i:i+3]) #sum bottom row

			total = top + middle + bottom
			maxSum = max(maxSum, total)
	return maxSum

class Test(unittest.TestCase):
	def test_all_positives(self):
		arr = [[1, 1, 1, 0, 0, 0],
				[0, 1, 0, 0, 0, 0],
				[1, 1, 1, 0, 0, 0],
				[0, 0, 2, 4, 4, 0],
				[0, 0, 0, 2, 0, 0],
				[0, 0, 1, 2, 4, 0]]
		self.assertEquals(hourglassSum(arr), 19)

	def test_some_negatives(self):
		arr = [[1, 1, 1, 0, 0, 0],
				[0, 1, 0, 0, 0, 0],
				[1, 1, 1, 0, 0, 0],
				[0, 9, 2, -4, -4, 0],
				[0, 0, 0, -2, 0, 0],
				[0, 0, -1, -2, -4, 0]]
		self.assertEquals(hourglassSum(arr), 13)

	def test_all_negatives(self):
		arr = [[-1, -1, -1, 0, 0, 0],
				[0, -1, 0, 0, 0, 0],
				[-1, -1, -1, 0, 0, 0],
				[0, 0, -2, -4, -4, 0],
				[0, 0, 0, -2, 0, 0],
				[0, 0, -1, -2, -4, 0]]
		self.assertEquals(hourglassSum(arr), 0)

if __name__ == "__main__":
	unittest.main()